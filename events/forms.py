import re
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Participant


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            'full_name',
            'phone_number',
            'tg_username',
            'startup_name',
            'startup_description',
            'startup_status',
            'startup_sphere',
            'startup_sphere_other',
            'position_in_startup',
            'has_entrepreneurship_experience',
            'has_attracted_investment',
            'incubators_accelerators',
            'presentation_link',
            'consent',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите ваше имя')}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите номер телефона')}),
            'tg_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите Telegram username')}),
            'startup_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите название стартапа')}),
            'startup_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Введите краткую информацию о стартапе'), 'rows': 4}),
            'startup_status': forms.Select(attrs={'class': 'form-control custom-select'}),
            'startup_sphere': forms.Select(attrs={'class': 'form-control custom-select'}),
            'startup_sphere_other': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Если другое, напишите')}),
            'position_in_startup': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите вашу должность в стартапе')}),
            'has_entrepreneurship_experience': forms.Select(attrs={'class': 'form-control custom-select'}),
            'has_attracted_investment': forms.Select(attrs={'class': 'form-control custom-select'}),
            'incubators_accelerators': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Введите информацию об инкубаторах и акселераторах'), 'rows': 3}),
            'presentation_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите ссылку на презентацию стартапа')}),
            'consent': forms.Select(attrs={'class': 'form-control custom-select'}),
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

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number or not phone_number.strip():
            raise forms.ValidationError(_('Номер телефона не может быть пустым.'))
        return phone_number

    def clean_tg_username(self):
        tg_username = self.cleaned_data.get('tg_username')
        if tg_username and not re.match(r'^@?[a-zA-Z0-9_]{3,32}$', tg_username.strip()):
            raise forms.ValidationError(_('Введите корректный Telegram username (например, @username).'))
        return tg_username

    def clean_startup_name(self):
        startup_name = self.cleaned_data.get('startup_name')
        if not startup_name or not startup_name.strip():
            raise forms.ValidationError(_('Название стартапа не может быть пустым.'))
        if len(startup_name.strip()) < 2:
            raise forms.ValidationError(_('Название стартапа должно содержать не менее 2 символов.'))
        if len(startup_name.strip()) > 100:
            raise forms.ValidationError(_('Название стартапа не может превышать 100 символов.'))
        return startup_name

    def clean_startup_description(self):
        startup_description = self.cleaned_data.get('startup_description')
        if not startup_description or not startup_description.strip():
            raise forms.ValidationError(_('Краткая информация о стартапе не может быть пустой.'))
        if len(startup_description.strip()) > 500:
            raise forms.ValidationError(_('Краткая информация о стартапе не может превышать 500 символов.'))
        return startup_description

    def clean_startup_sphere_other(self):
        startup_sphere = self.cleaned_data.get('startup_sphere')
        startup_sphere_other = self.cleaned_data.get('startup_sphere_other')
        if startup_sphere == 'other' and not startup_sphere_other.strip():
            raise forms.ValidationError(_('Если выбрано "Другое", необходимо указать сферу стартапа.'))
        return startup_sphere_other

    def clean_position_in_startup(self):
        position_in_startup = self.cleaned_data.get('position_in_startup')
        if not position_in_startup or not position_in_startup.strip():
            raise forms.ValidationError(_('Ваша должность в стартапе не может быть пустой.'))
        if len(position_in_startup.strip()) > 200:
            raise forms.ValidationError(_('Ваша должность в стартапе не может превышать 200 символов.'))
        return position_in_startup

    def clean_presentation_link(self):
        presentation_link = self.cleaned_data.get('presentation_link')
        if not presentation_link or not presentation_link.strip():
            raise forms.ValidationError(_('Ссылка на презентацию стартапа не может быть пустой.'))
        return presentation_link

    def clean_consent(self):
        consent = self.cleaned_data.get('consent')
        if not consent:
            raise forms.ValidationError(_('Вы должны согласиться с условиями, чтобы продолжить.'))
        return consent