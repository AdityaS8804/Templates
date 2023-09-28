from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea, TextInput, CharField
class UserAdminConfig(UserAdmin):
    model=NewUser
    search_fields=('email','user_name','first_name',)
    list_filter=('email','user_name','first_name','is_active','is_staff',)
    ordering=('-start_date',)
    list_display=('email','user_name','first_name','is_active','is_staff',)
    fieldsets = (
        (None, {
            "fields": (
                'email', 'user_name','first_name',
            ),
        }),
        #('Permissions', {'fields':()}),
        ('Personal',{'fields':('about',)})
    )
    formfields_overrides={
        models.TextField:{'widget':Textarea(attrs={'rows':20, 'cols':20})}
    }
    add_fieldsets=(
        (
            None, {
                'classes':('wide', ),
                'fields':('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active','is_staff',)
            }
        )
    )
    

# Register your models here.
admin.site.register(NewUser, UserAdminConfig)