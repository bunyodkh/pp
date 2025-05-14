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
            partner = form.save(commit=False)
            partner.registration_source = 'website'
            partner.save()
            messages.success(request, _('Ваша заявка успешно отправлена.'))
            return redirect('partners:partner-list')
        else:
            messages.error(request, _('Произошла ошибка при отправке заявки. Пожалуйста, исправьте ошибки ниже.'))
    else:
        form = PartnerForm()

    return render(request, 'partner_list.html', {'form': form})
