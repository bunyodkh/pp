from django.shortcuts import render, get_list_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import PartnerForm

def partner_add(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your application has been successfully submitted.'))
            return redirect('mentors:mentor-add')
        else:
            messages.error(request, _('There was an error submitting your application. Please correct the errors below.'))
    else:
        form = PartnerForm()

    return render(request, 'partner_add.html', {'form': form})
