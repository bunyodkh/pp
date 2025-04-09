from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils.translation import gettext as _

from events.models import Event
from partners.models import Partner

def index(request):
    event = get_object_or_404(Event, show_on_main=True)
    partners = get_list_or_404(Partner)
    return render(request, 'index.html', { 'event': event, 'partners': partners })