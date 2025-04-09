import re
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Participant

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        
        fields = [
            'full_name',
            'institution',
            'tg',
            'email',
            'project',
            'role',
            'link',
            'description'
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'tg': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not full_name or not full_name.strip():
            raise forms.ValidationError(_('Full name cannot be empty.'))
        if len(full_name.strip()) < 2:
            raise forms.ValidationError(_('Full name must be at least 2 characters long.'))
        if len(full_name.strip()) > 100:
            raise forms.ValidationError(_('Full name cannot exceed 100 characters.'))
        return full_name
    

    def clean_institution(self):
        institution = self.cleaned_data.get('institution')
        if not institution or not institution.strip():
            raise forms.ValidationError(_('Institution cannot be empty.'))
        if len(institution.strip()) < 2:
            raise forms.ValidationError(_('Institution must be at least 2 characters long.'))
        if len(institution.strip()) > 100:
            raise forms.ValidationError(_('Institution cannot exceed 100 characters.'))
        return institution
    

    def clean_tg(self):
        tg = self.cleaned_data.get('tg')
        if not tg or not tg.strip():
            raise forms.ValidationError(_('Telegram cannot be empty.'))
        if len(tg.strip()) < 2:
            raise forms.ValidationError(_('Telegram must be at least 2 characters long.'))
        if len(tg.strip()) > 100:
            raise forms.ValidationError(_('Telegram cannot exceed 100 characters.'))
        return tg
    

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
    

    def clean_project(self):
        project = self.cleaned_data.get('project')
        if not project or not project.strip():
            raise forms.ValidationError(_('Project name cannot be empty.'))
        if len(project.strip()) < 2:
            raise forms.ValidationError(_('Project name must be at least 2 characters long.'))
        if len(project.strip()) > 100:
            raise forms.ValidationError(_('Project name cannot exceed 100 characters.'))
        return project
    

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if not role or not role.strip():
            raise forms.ValidationError(_('Role cannot be empty.'))
        if len(role.strip()) < 2:
            raise forms.ValidationError(_('Role must be at least 2 characters long.'))
        if len(role.strip()) > 100:
            raise forms.ValidationError(_('Role cannot exceed 100 characters.'))
        return role
    

    def clean_link(self):
        link = self.cleaned_data.get('link')
        if not link or not link.strip():
            raise forms.ValidationError(_('Link cannot be empty.'))
        if len(link.strip()) < 2:
            raise forms.ValidationError(_('Link must be at least 2 characters long.'))
        if len(link.strip()) > 500:
            raise forms.ValidationError(_('Link cannot exceed 500 characters.'))
        # Regex validation: Must be a valid URL format
        if link and not re.match(r'^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/[\w\-]*)*$', link.strip()):
            raise forms.ValidationError(_('Enter a valid website URL (e.g., https://example.com).'))
        return link