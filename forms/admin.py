from django.contrib import admin

from .models import Field, Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass
