from django.contrib import admin
from .models import Ticket, TicketCategory, TicketImage


class TicketImageInline(admin.TabularInline):
    model = TicketImage
    extra = 1


@admin.register(TicketCategory)
class TicketCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "student", "category", "status", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "message", "student__phone_number")
    autocomplete_fields = ("student", "category")
    inlines = [TicketImageInline]


@admin.register(TicketImage)
class TicketImageAdmin(admin.ModelAdmin):
    list_display = ("ticket", "image")
