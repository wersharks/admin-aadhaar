from django.contrib import admin
from .models import Operator

# Register your models here.

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('picture',)
