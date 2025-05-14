import re
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Partner

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        
        fields = [
            'name',
            'email',
            'phone',
            'website',
            'reason',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
        }
        

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name.strip():
            raise forms.ValidationError(_('Имя не может быть пустым.'))
        if len(name.strip()) < 2:
            raise forms.ValidationError(_('Имя должно быть длиной не менее 2 символов.'))
        if len(name.strip()) > 100:
            raise forms.ValidationError(_('Имя не может превышать 100 символов.'))
        # Regex validation: Only letters and spaces allowed
        if not re.match(r'^[a-zA-Z\s]+$', name.strip()):
            raise forms.ValidationError(_('Имя может содержать только буквы и пробелы.'))
        return name
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or not email.strip():
            raise forms.ValidationError(_('Электронная почта не может быть пустой.'))
        if len(email.strip()) > 100:
            raise forms.ValidationError(_('Длина адреса электронной почты не может превышать 100 символов.'))
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email.strip()):
            raise forms.ValidationError(_('Введите действительный адрес электронной почты (т. е. необходимо включить знак @).'))
        return email


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or not phone.strip():
            raise forms.ValidationError(_('Номер телефона не может быть пустым.'))
        if len(phone.strip()) < 9:
            raise forms.ValidationError(_('Номер телефона должен содержать не менее 10 символов.'))
        if len(phone.strip()) > 13:
            raise forms.ValidationError(_('Номер телефона не может превышать 15 символов.'))
        # Regex validation: Must be a valid phone number format
        if not re.match(r'^\+?[0-9]{10,15}$', phone.strip()):
            raise forms.ValidationError(_('Введите действительный номер телефона (например, +1234567890).'))
        return phone
    

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website and not website.strip():
            raise forms.ValidationError(_('Сайт не может быть пустым.'))
        if website and len(website.strip()) > 50:
            raise forms.ValidationError(_('URL-адрес веб-сайта не может превышать 50 символов.'))
        # Regex validation: Must be a valid URL format
        if website and not re.match(r'^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/[\w\-]*)*$', website.strip()):
            raise forms.ValidationError(_('Введите действительный URL-адрес веб-сайта (например, https://example.com).'))
        return website