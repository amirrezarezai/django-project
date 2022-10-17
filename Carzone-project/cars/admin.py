from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=30px style="border-radius:50px;"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'car image'
    list_display = ('id','thumbnail','car_title','city','color','model','is_featured')
    list_filter = ('city','model','body_style')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','model','city')
    list_display_links = ('id','thumbnail')

admin.site.register(Car,CarAdmin)