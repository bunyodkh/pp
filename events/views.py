from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import HttpResponseBadRequest

from .models import Event
from .forms import RegistrationForm


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


def event_registration(request, event_number):
    # Fetch the event or return a 404 if not found
    event = get_object_or_404(Event, event_number=event_number)

    if request.method == 'POST':
        print(request.POST)  # Debugging line to check the POST data
        form = RegistrationForm(request.POST)
        print(form.is_valid())  # Debugging line to check if the form is valid
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = event
            participant.save()
            messages.success(request, _('You have successfully registered for the event.'))
            return redirect(event.get_absolute_url())  # Redirect to the event's absolute URL
        else:
            messages.error(request, _('There was an error with your registration. Please try again.'))
    else:
        form = RegistrationForm()

    # Render the registration page with the form and event details
    return render(request, 'event_registration.html', {'form': form, 'event': event})

