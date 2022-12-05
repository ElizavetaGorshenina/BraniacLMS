from django.contrib import admin

from authapp import models as authapp_models


@admin.register(authapp_models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "age", "email", "is_staff", "is_active"]
    search_fields = ["username", "age", "email"]
    ordering = ["username", "is_active"]
    list_per_page = 20
    list_filter = ["username", "age", "is_staff", "is_active"]
