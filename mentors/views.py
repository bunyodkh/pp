from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.messages import get_messages

from .models import Mentor
from .forms import MentorForm


def mentor_list(request):
    mentors = Mentor.objects.filter(show_on_page=True).order_by('-created_at')
    form = MentorForm()
    return render(request, 'mentor_list.html', {'mentors': mentors, 'form': form})



def mentor_add(request):
    mentors = Mentor.objects.filter(show_on_page=True).order_by('-created_at')

    # Always initialize form
    form = MentorForm()

    # Check for success message (from previous POST redirect)
    storage = get_messages(request)
    form_success = any(message.tags == 'success' for message in storage)
    storage.used = False  # allow template to read messages again

    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.registration_source = 'website'
            mentor.save()
            messages.success(request, _('Your application has been submitted successfully!'))
            return redirect('mentors:mentor-add')  # <- must match the same view name

    return render(request, 'mentor_list.html', {
        'form': form,
        'mentors': mentors,
        'form_success': form_success,
    })
