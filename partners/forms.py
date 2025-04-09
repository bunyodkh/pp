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
            raise forms.ValidationError(_('Name cannot be empty.'))
        if len(name.strip()) < 2:
            raise forms.ValidationError(_('Name must be at least 2 characters long.'))
        if len(name.strip()) > 100:
            raise forms.ValidationError(_('Name cannot exceed 100 characters.'))
        # Regex validation: Only letters and spaces allowed
        if not re.match(r'^[a-zA-Z\s]+$', name.strip()):
            raise forms.ValidationError(_('Name can only contain letters and spaces.'))
        return name
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or not email.strip():
            raise forms.ValidationError(_('Email cannot be empty.'))
        if len(email.strip()) > 100:
            raise forms.ValidationError(_('Email cannot exceed 100 characters.'))
        # Regex validation: Must be a valid email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email.strip()):
            raise forms.ValidationError(_('Enter a valid email address (i.e., @ sign should be included.).'))
        return email


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or not phone.strip():
            raise forms.ValidationError(_('Phone number cannot be empty.'))
        if len(phone.strip()) < 9:
            raise forms.ValidationError(_('Phone number must be at least 10 characters long.'))
        if len(phone.strip()) > 13:
            raise forms.ValidationError(_('Phone number cannot exceed 15 characters.'))
        # Regex validation: Must be a valid phone number format
        if not re.match(r'^\+?[0-9]{10,15}$', phone.strip()):
            raise forms.ValidationError(_('Enter a valid phone number (e.g., +1234567890).'))
        return phone
    

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website and not website.strip():
            raise forms.ValidationError(_('Website cannot be empty.'))
        if website and len(website.strip()) > 50:
            raise forms.ValidationError(_('Website URL cannot exceed 50 characters.'))
        # Regex validation: Must be a valid URL format
        if website and not re.match(r'^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/[\w\-]*)*$', website.strip()):
            raise forms.ValidationError(_('Enter a valid website URL (e.g., https://example.com).'))
        return website