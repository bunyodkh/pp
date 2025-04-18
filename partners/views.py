from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import PartnerForm
from .models import Partner


def partner_list(request):
    partners = Partner.objects.filter(show_on_website=True).order_by('-created_at')
    form = PartnerForm()
    return render(request, 'partner_list.html', {'partners': partners, 'form': form})


def partner_add(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your application has been successfully submitted.'))
            return redirect('mentors:mentor-list')
        else:
            messages.error(request, _('There was an error submitting your application. Please correct the errors below.'))
    else:
        form = PartnerForm()

    return render(request, 'partner_list.html', {'form': form})
