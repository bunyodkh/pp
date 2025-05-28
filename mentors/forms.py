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
            raise forms.ValidationError(_('Полное имя не может быть пустым.'))
        if len(full_name.strip()) < 2:
            raise forms.ValidationError(_('Полное имя должно содержать не менее 2 символов.'))
        if len(full_name.strip()) > 100:
            raise forms.ValidationError(_('Полное имя не может превышать 100 символов.'))
        return full_name
    
    def clean_organization(self):
        organization = self.cleaned_data.get('organization')
        if not organization or not organization.strip():
            raise forms.ValidationError(_('Организация не может быть пустой.'))
        if len(organization.strip()) < 2:
            raise forms.ValidationError(_('Название организации должно содержать не менее 2 символов.'))
        if len(organization.strip()) > 100:
            raise forms.ValidationError(_('Название организации не может превышать 100 символов.'))
        return organization

    def clean_position(self):
        position = self.cleaned_data.get('position')
        if not position or not position.strip():
            raise forms.ValidationError(_('Должность не может быть пустой.'))
        if len(position.strip()) < 2:
            raise forms.ValidationError(_('Должность должна содержать не менее 2 символов.'))
        if len(position.strip()) > 100:
            raise forms.ValidationError(_('Должность не может превышать 100 символов.'))
        return position

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or not phone.strip():
            raise forms.ValidationError(_('Номер телефона не может быть пустым.'))
        if len(phone.strip()) < 9:
            raise forms.ValidationError(_('Номер телефона должен содержать не менее 9 символов.'))
        if len(phone.strip()) > 15:
            raise forms.ValidationError(_('Номер телефона не может превышать 15 символов.'))
        return phone

    def clean_tg(self):
        tg = self.cleaned_data.get('tg')
        if not tg or not tg.strip():
            raise forms.ValidationError(_('Имя пользователя Telegram не может быть пустым.'))
        if len(tg.strip()) < 2:
            raise forms.ValidationError(_('Имя пользователя Telegram должно содержать не менее 2 символов.'))
        if len(tg.strip()) > 50:
            raise forms.ValidationError(_('Имя пользователя Telegram не может превышать 50 символов.'))
        return tg

    def clean_linkedin_profile(self):
        linkedin_profile = self.cleaned_data.get('linkedin_profile')
        if not linkedin_profile or not linkedin_profile.strip():
            raise forms.ValidationError(_('Профиль LinkedIn не может быть пустым.'))
        if len(linkedin_profile.strip()) < 10:
            raise forms.ValidationError(_('Профиль LinkedIn должен содержать не менее 10 символов.'))
        if len(linkedin_profile.strip()) > 200:
            raise forms.ValidationError(_('Профиль LinkedIn не может превышать 200 символов.'))
        return linkedin_profile
