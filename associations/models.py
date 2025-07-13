from django.db import models
from django.utils.translation import gettext_lazy as _


class Association(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام انجمن")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "انجمن"
        verbose_name_plural = "انجمن‌ها"
        ordering = ["name"]

    def __str__(self):
        return self.name
