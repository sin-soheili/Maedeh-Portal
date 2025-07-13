import os
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def ticket_image_upload_path(instance, filename):
    return f"tickets/{instance.ticket.id}/{filename}"


class TicketCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته‌بندی")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = "دسته‌بندی تیکت"
        verbose_name_plural = "دسته‌بندی‌های تیکت"

    def __str__(self):
        return self.title


class Ticket(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("در انتظار بررسی")
        ANSWERED = "answered", _("پاسخ داده شده")
        CLOSED = "closed", _("بسته شده")

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="دانشجو",
        related_name="tickets",
    )
    category = models.ForeignKey(
        TicketCategory,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="دسته‌بندی"
    )
    title = models.CharField(max_length=255, verbose_name="عنوان")
    message = models.TextField(verbose_name="متن پیام")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="وضعیت"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت‌ها"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.student}"


class TicketImage(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="تیکت مربوطه"
    )
    image = models.ImageField(upload_to=ticket_image_upload_path, verbose_name="تصویر")

    class Meta:
        verbose_name = "تصویر تیکت"
        verbose_name_plural = "تصاویر تیکت"

    def __str__(self):
        return os.path.basename(self.image.name)
