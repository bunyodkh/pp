from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _

from events.models import Event, EventType
from partners.models import Partner
from mentors.models import Mentor

def index(request):
    event = Event.objects.filter(show_on_main=True, active=True).first()
    event_types = EventType.objects.filter(show_on_main=True)
    partners = Partner.objects.filter(show_on_website=True).order_by('-created_at')
    mentors = Mentor.objects.filter(show_on_main=True).order_by('-created_at')

    print(event_types)

    return render(request, 'index.html', { 
        'event': event, 
        'partners': partners, 
        'mentors': mentors, 
        'event_types': event_types,
    })