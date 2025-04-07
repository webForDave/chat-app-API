from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = ["email", "is_staff", "is_active"]
    list_filter = ["email", "is_staff", "is_active"]
    fieldsets = ((None, {"fields": ("email",)}),)
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active")
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUserModel, CustomUserAdmin)