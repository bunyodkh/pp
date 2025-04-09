from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Partner

@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    pass
