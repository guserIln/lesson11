from django.contrib import admin
from core import models
# Register your models here.
@admin.register(models.Visit)
class Visit(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Patient)
class Patient(admin.ModelAdmin):
    list_display = ('first_name', 'second_name',)