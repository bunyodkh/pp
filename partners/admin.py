from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Partner

@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    list_display = ('name', 'registration_source', 'show_on_website')
    list_filter = ('registration_source', 'show_on_website')

