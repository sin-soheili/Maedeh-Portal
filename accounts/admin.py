from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("phone_number", "is_active", "is_staff", "is_superuser", "is_verified")
    list_filter = ("is_active", "is_staff", "is_superuser", "is_verified")
    search_fields = ("phone_number", "email", "first_name", "last_name")

    fieldsets = (
        (_("اطلاعات اصلی"), {
            "fields": ("phone_number", "email", "password")
        }),
        (_("اطلاعات شخصی"), {
            "fields": ("first_name", "last_name", "username", "student_id")
        }),
        (_("دسترسی‌ها"), {
            "fields": ("is_active", "is_staff", "is_superuser", "is_verified", "groups", "user_permissions")
        }),
        (_("تاریخ‌ها"), {
            "fields": ("last_login", "created_at")
        }),
    )

    add_fieldsets = (
        (_("افزودن کاربر"), {
            "classes": ("wide",),
            "fields": ("phone_number", "username", "student_id", "first_name", "last_name", "email", "password1", "password2", "is_active", "is_staff", "is_superuser"),
        }),
    )
