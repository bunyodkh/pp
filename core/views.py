from django.shortcuts import render
from django.utils.translation import gettext as _

from events.models import Event
from partners.models import Partner
from mentors.models import Mentor

def index(request):
    event = Event.objects.get(show_on_main=True)
    partners = Partner.objects.filter(show_on_website=True).order_by('-created_at')
    mentors = Mentor.objects.filter(show_on_website=True).order_by('-created_at')
    return render(request, 'index.html', { 'event': event, 'partners': partners, 'mentors': mentors })