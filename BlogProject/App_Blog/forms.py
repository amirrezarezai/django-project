from django import forms
from App_Blog.models import Blog,comment

class Commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment',)