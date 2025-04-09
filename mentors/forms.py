import re
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Mentor


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = [
            'full_name', 
            'organization',
            'position', 
            'tg',
            'phone', 
            'reason', 
            'linkedin_profile', 
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control' }),
            'organization': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'required': False }),
            'tg': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'linkedin_profile': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
        }
 
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not full_name or not full_name.strip():
            raise forms.ValidationError(_('Full name cannot be empty.'))
        if len(full_name.strip()) < 2:
            raise forms.ValidationError(_('Full name must be at least 2 characters long.'))
        if len(full_name.strip()) > 100:
            raise forms.ValidationError(_('Full name cannot exceed 100 characters.'))
        # Regex validation: Only letters and spaces allowed
        if not re.match(r'^[a-zA-Z\s]+$', full_name.strip()):
            raise forms.ValidationError(_('Full name can only contain letters and spaces.'))
        return full_name
    
    def clean_organization(self):
        organization = self.cleaned_data.get('organization')
        if not organization or not organization.strip():
            raise forms.ValidationError(_('Organization cannot be empty.'))
        if len(organization.strip()) < 2:
            raise forms.ValidationError(_('Organization must be at least 2 characters long.'))
        if len(organization.strip()) > 100:
            raise forms.ValidationError(_('Organization cannot exceed 100 characters.'))
        # Regex validation: Only letters, numbers, spaces, and special characters like "-" and "&" allowed
        if not re.match(r'^[a-zA-Z0-9\s\-\&]+$', organization.strip()):
            raise forms.ValidationError(_('Organization can only contain letters, numbers, spaces, hyphens, and ampersands.'))
        return organization

    def clean_position(self):
        position = self.cleaned_data.get('position')
        if not position or not position.strip():
            raise forms.ValidationError(_('Position cannot be empty.'))
        if len(position.strip()) < 2:
            raise forms.ValidationError(_('Position must be at least 2 characters long.'))
        if len(position.strip()) > 100:
            raise forms.ValidationError(_('Position cannot exceed 100 characters.'))
        # Regex validation: Only letters, spaces, and special characters like "-" allowed
        if not re.match(r'^[a-zA-Z\s\-]+$', position.strip()):
            raise forms.ValidationError(_('Position can only contain letters, spaces, and hyphens.'))
        return position

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

    def clean_tg(self):
        tg = self.cleaned_data.get('tg')
        if not tg or not tg.strip():
            raise forms.ValidationError(_('Telegram username cannot be empty.'))
        if len(tg.strip()) < 2:
            raise forms.ValidationError(_('Telegram username must be at least 2 characters long.'))
        if len(tg.strip()) > 50:
            raise forms.ValidationError(_('Telegram username cannot exceed 50 characters.'))
        # Regex validation: Must start with '@' and contain only letters, numbers, and underscores
        if not re.match(r'^@[a-zA-Z0-9_]+$', tg.strip()):
            raise forms.ValidationError(_('Telegram username must start with "@" and contain only letters, numbers, and underscores.'))
        return tg

    def clean_linkedin_profile(self):
        linkedin_profile = self.cleaned_data.get('linkedin_profile')
        if not linkedin_profile or not linkedin_profile.strip():
            raise forms.ValidationError(_('LinkedIn profile cannot be empty.'))
        if len(linkedin_profile.strip()) < 2:
            raise forms.ValidationError(_('LinkedIn profile must be at least 10 characters long.'))
        if len(linkedin_profile.strip()) > 200:
            raise forms.ValidationError(_('LinkedIn profile cannot exceed 200 characters.'))
        # Regex validation: Must be a valid LinkedIn URL
        if not re.match(r'^https://(www\.)?linkedin\.com/.*$', linkedin_profile.strip()):
            raise forms.ValidationError(_('Enter a valid LinkedIn profile URL (e.g., https://www.linkedin.com/in/username).'))
        return linkedin_profile
