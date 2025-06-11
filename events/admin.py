from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from import_export.admin import ImportExportModelAdmin
from .resources import ParticipantModelResource


from .models import EventType, Event, Participant, EventPhoto, Achievement,EventWinner, EventTimeline


class EventPhotoInline(TabularInline):  # or admin.StackedInline for a different layout
    model = EventPhoto
    extra = 1  # Number of empty forms to display for adding new photos


# class EventParticipantsInline(TabularInline):
#     model = Participant
#     extra = 1  # Number of empty forms to display for adding new participants


@admin.register(Event)
class EventAdmin(ModelAdmin):
     list_display = ('name', 'event_type', 'planned_date', 'active')
     inlines = [EventPhotoInline]  # Include the inline class here

from import_export.formats import base_formats

@admin.register(Participant)
class ParticipantAdmin(ImportExportModelAdmin):
    resource_class = ParticipantModelResource
    list_display = ('full_name', 'startup_name', 'phone_number', 'event')

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.XLSX,
            # base_formats.CSV,
        )
        # This will return only the formats that have their
        # required dependencies installed.
        return [f for f in formats if f().can_export()]

@admin.register(EventType)
class EventTypeAdmin(ModelAdmin):
    pass    

@admin.register(Achievement)
class AchievementAdmin(ModelAdmin):
    pass    

@admin.register(EventWinner)
class EventWinnerAdmin(ModelAdmin):
    pass


@admin.register(EventTimeline)
class EventTimelineAdmin(ModelAdmin):
    pass