from django.db import models
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    event_type = models.ManyToManyField('events.EventType', related_name='partners', verbose_name=_('Тип мероприятия'), blank=True)
    name = models.CharField(_('Название'), max_length=200, blank=True, null=True, help_text=_('Название на русском языке'))
    name_en = models.CharField(_('Название на английском'), max_length=200, blank=True, null=True, help_text=_('Название на английском языке'))
    name_uz = models.CharField(_('Название на узбекском'), max_length=200, blank=True, null=True, help_text=_('Название на узбекском языке'))

    email = models.CharField(_('Электронная почта'), max_length=200, blank=True, null=True)
    phone = models.CharField(_('Телефон'), max_length=20, blank=True, null=True)
    website = models.CharField(_('Сайт'), max_length=200, blank=True, null=True)
    reason = models.TextField(_('Почему хотите стать партнером?'), blank=True, null=True)
    logo = models.ImageField(_('Логотипа'), upload_to='partners/', blank=True, null=True)

    show_on_main = models.BooleanField(_('Показать на главной странице'), default=False)
    show_on_website = models.BooleanField(_('Показать на сайте'), default=False)

    registration_source = models.CharField(max_length=50, choices=[('website', 'Website'), ('admin', 'Admin')], default='admin', verbose_name=_('Источник регистрации'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.created_at}'
        
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Партнер')
        verbose_name_plural = _('Партнеры')
    
