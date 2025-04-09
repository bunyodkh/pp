from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Mentor
from .forms import MentorForm


def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentor_list.html', {'mentors': mentors})


def mentor_add(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your application has been successfully submitted.'))
            return redirect('mentors:mentor-add')
        else:
            messages.error(request, _('There was an error submitting your application. Please correct the errors below.'))
    else:
        form = MentorForm()

    return render(request, 'mentor_add.html', {'form': form})