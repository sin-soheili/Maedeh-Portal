from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from core.validators import validate_iranian_cellphone
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("شماره تلفن الزامی است.")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("نام کاربری", max_length=25,unique=True)
    student_id = models.CharField("شماره دانشجویی", max_length=15, unique=True)
    first_name = models.CharField("نام", max_length=50)
    last_name = models.CharField("نام خانوادگی", max_length=50)
    phone_number = models.CharField("شماره تلفن", max_length=11, unique=True, validators=[validate_iranian_cellphone])
    email = models.EmailField("ایمیل", blank=True, null=True)
    is_active = models.BooleanField("فعال", default=True)
    is_staff = models.BooleanField("کارمند", default=False)
    is_verified = models.BooleanField("تأیید شده", default=False)
    created_at = models.DateTimeField("تاریخ ثبت‌نام", default=timezone.now)
    updated_at = models.DateTimeField("آخرین بروزرسانی", auto_now=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['student_id', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
