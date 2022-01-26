from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.customUser)
class customUseradmin(admin.ModelAdmin):
    list_display = ['user_id', 'type', 'email', 'verified']

