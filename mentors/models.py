from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Mentor(models.Model):
    full_name = models.CharField(_('Имя и фамилия'), max_length=100, blank=True, null=True)
    full_name_en = models.CharField(_('Имя и фамилия на английском'), max_length=100, blank=True, null=True)
    full_name_uz = models.CharField(_('Имя и фамилия на узбекском'), max_length=100, blank=True, null=True)

    organization = models.CharField(_('Название организации'), max_length=100, blank=True, null=True)
    organization_en = models.CharField(_('Название организации на английском'), max_length=100, blank=True, null=True)
    organization_uz = models.CharField(_('Название организации на узбекском'), max_length=100, blank=True, null=True)

    position = models.CharField(_('Должность'), max_length=100, blank=True, null=True)
    position_en = models.CharField(_('Должность на английском'), max_length=100, blank=True, null=True)
    position_uz = models.CharField(_('Должность на узбекском'), max_length=100, blank=True, null=True)

    phone = models.CharField(_('Номер телефона'), max_length=15, blank=True, null=True)
    tg = models.CharField(_('Telegram'), max_length=15, blank=True, null=True)
    linkedin_profile = models.CharField(_('Linkedin'), max_length=100, blank=True, null=True)
    reason = models.TextField(_('Почему хотите стать ментором?'), blank=True, null=True)
    photo = models.ImageField(_('Фотография'), upload_to='mentors/', blank=True, null=True)

    show_on_main = models.BooleanField(_('Показать на главной странице'), default=False)
    show_on_page = models.BooleanField(_('Показать на странице менторов'), default=False)

    registration_source = models.CharField(max_length=50, choices=[('website', 'Website'), ('admin', 'Admin')], default='admin', verbose_name=_('Источник регистрации'))


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} {self.created_at}'
    
    def get_absolute_url(self):
        return reverse('mentor_detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = _('Наставник')
        verbose_name_plural = _('Наставники')
        
        
