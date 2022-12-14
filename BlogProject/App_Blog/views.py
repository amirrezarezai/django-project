from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,TemplateView,DetailView,DeleteView,UpdateView,ListView
from App_Blog.models import Blog,likes,comment
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from App_Blog.forms import Commentform
# Create your views here.
class myBlog(LoginRequiredMixin,TemplateView):
    template_name = 'App_Blog/my_blog.html'

class updateBlog(LoginRequiredMixin,UpdateView):
    template_name = 'App_Blog/edit_blog.html'
    model = Blog
    fields = ('blog_title','blog_content','blog_image')

    def get_success_url(self,**kwargs):
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug':self.object.slug})


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    queryset = Blog.objects.order_by('-publish_date')

class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','-') + '-' + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = Commentform()
    already_like = likes(blog=blog,user=request.user)
    if already_like:
        liked = True
    else:
        liked = False

    if request.method == 'POST':
        comment_form = Commentform(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':slug}))


    return render(request,'App_Blog/blog_details.html',context = {'blog':blog,'comment':comment_form,'liked':liked})

@login_required
def like(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post = likes(blog=blog,user=user)
        liked_post.save()

    return HttpResponseRedirect(reverse('App_Blog:blog_details' , kwargs={'slug':blog.slug}))


@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = likes.objects.filter(blog=blog,user=user)
    already_liked.delete()

    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': blog.slug}))




