from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Mentor

@admin.register(Mentor)
class MentorAdmin(ModelAdmin):
    list_display = ('full_name', 'registration_source', 'show_on_website')
    list_filter = ('registration_source', 'show_on_website')
