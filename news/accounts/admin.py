from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

class UserAdmin(UserAdmin):
    fieldsets = (
        ('System credentials', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('role', )})
    )

admin.site.register(User, UserAdmin)