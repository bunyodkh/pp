from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import EventType
from .forms import RegistrationForm


def event_type_detail(request, slug):
    event_type = get_object_or_404(EventType, slug=slug)
    active_event = event_type.event_set.filter(active=True).first()

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
        form = RegistrationForm()
   
    return render(request, 'event_detail.html', {'event_type': event_type, 'event':active_event, 'form': form})


