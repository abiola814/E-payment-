from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instance

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email')
  

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.



    search_fields = ('email','name')
    ordering = ('email','username')
    filter_horizontal = ()



admin.site.register(User, UserAdmin)

