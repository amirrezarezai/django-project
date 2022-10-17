from django.contrib import admin
from .models import Contacts
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','city','create_date')
    list_display_links = ('id','first_name')
    search_fields = ('email','first_name','create_date')
    list_per_page = 25

admin.site.register(Contacts,ContactAdmin)