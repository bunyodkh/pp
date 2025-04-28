from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import EventType
from .forms import RegistrationForm


def event_type_detail(request, slug):
    event_type = get_object_or_404(EventType, slug=slug)
    active_event = event_type.events.filter(active=True).first()
    past_events = event_type.events.filter(active=False).order_by('-planned_date')
    partners = event_type.partners.all() 
    achievements = event_type.achievements.all()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = active_event
            participant.save()
            messages.success(request, _('You have successfully registered for the event.'))
            return redirect(event_type.get_absolute_url())  # Redirect to the event's absolute URL
        else:
            messages.error(request, _('There was an error with your registration. Please try again.'))
    else:
        if not active_event:
            return render(request, 'event_detail.html', {
                    'event_type': event_type, 
                    'partners': partners, 
                    'achievements': achievements , 
                    'past_events': past_events
                })
        form = RegistrationForm()
   
    return render(request, 'event_detail.html', {
            'event_type': event_type, 
            'event':active_event, 
            'form': form, 'partners': partners, 
            'achievements': achievements, 
            'past_events': past_events
        })


