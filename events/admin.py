from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import EventType, Event, Participant, EventPhoto, Achievement


class EventPhotoInline(TabularInline):  # or admin.StackedInline for a different layout
    model = EventPhoto
    extra = 1  # Number of empty forms to display for adding new photos


class EventParticipantsInline(TabularInline):
    model = Participant
    extra = 1  # Number of empty forms to display for adding new participants


@admin.register(Event)
class EventAdmin(ModelAdmin):
     inlines = [EventPhotoInline, EventParticipantsInline]  # Include the inline class here


@admin.register(Participant)
class ParticipantAdmin(ModelAdmin):
    pass

@admin.register(EventType)
class EventTypeAdmin(ModelAdmin):
    pass    

@admin.register(Achievement)
class AchievementAdmin(ModelAdmin):
    pass    