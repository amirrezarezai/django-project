from django.contrib import admin
from django.utils.html import format_html
from .models import Team
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=30px style="border-radius:50px;"/>'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id','thumbnail','first_name','designation','created_date')
    list_display_links = ('thumbnail','first_name',)
    search_fields = ('id','first_name','created_date',)
    list_filter = ('created_date','designation',)



admin.site.register(Team , TeamAdmin)