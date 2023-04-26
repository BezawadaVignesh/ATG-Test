from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, PProfile, DProfile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', )
    list_filter = ('Type', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'Type', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'Type', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(PProfile)
admin.site.register(DProfile)
