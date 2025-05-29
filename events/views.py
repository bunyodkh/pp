from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import EventType
from .forms import RegistrationForm


def event_type_detail(request, slug):
    event_type = get_object_or_404(EventType, slug=slug)
    active_event = event_type.events.filter(active=True).first()

    print(active_event)

    past_events = event_type.events.filter(active=False).order_by('-planned_date')
    partners = event_type.partners.all()
    achievements = event_type.achievements.all()

    # Initialize the form
    form = RegistrationForm()

    # Check for success message (from previous POST redirect)
    storage = messages.get_messages(request)
    form_success = any(message.tags == 'success' for message in storage)
    storage.used = True  

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = active_event
            participant.save()
            messages.success(request, _('Your application has been submitted successfully!'))
            return redirect(f'{event_type.get_absolute_url()}#submission-success')  # Redirect to the same page with anchor

    # Render the template
    return render(request, 'event_detail.html', {
        'event_type': event_type,
        'event': active_event,
        'form': form,
        'form_success': form_success,  # Pass form success to the template
        'partners': partners,
        'achievements': achievements,
        'past_events': past_events,
    })


