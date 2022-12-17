from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name', 'username')
    list_display_links = ('id', 'first_name','last_name', 'username')
    list_per_page = 20

admin.site.register(User, UserAdmin)