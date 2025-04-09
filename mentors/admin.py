from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Mentor

@admin.register(Mentor)
class MentorAdmin(ModelAdmin):
    pass
