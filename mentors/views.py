from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Mentor
from .forms import MentorForm


def mentor_list(request):
    mentors = Mentor.objects.filter(show_on_website=True).order_by('-created_at')
    form = MentorForm()
    return render(request, 'mentor_list.html', {'mentors': mentors, 'form': form})


def mentor_add(request):
    mentors = Mentor.objects.filter(show_on_website=True).order_by('-created_at')
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.registration_source = 'website'
            mentor.save()
            messages.success(request, _('Your application has been successfully submitted.'))
            return redirect('partners:partner-list')
        else:
            messages.error(request, _('There was an error submitting your application. Please correct the errors below.'))
    else:
        form = MentorForm()

    return render(request, 'mentor_list.html', {'form': form, 'mentors': mentors})