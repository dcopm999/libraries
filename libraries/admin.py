from django.contrib import admin

from libraries import models


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['token']
