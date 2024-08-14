from django.contrib import admin
from .models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone']
    search_fields = ['username', 'email', 'phone']
    list_filter = ['is_active', 'is_staff']
    ordering = ['id']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    search_fields = ['user__username']
    ordering = ['user']
