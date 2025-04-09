from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Mentor(models.Model):
    full_name = models.CharField(_('Имя и фамилия'), max_length=100, blank=True, null=True)
    organization = models.CharField(_('Название организации'), max_length=100, blank=True, null=True)
    position = models.CharField(_('Должность'), max_length=100, blank=True, null=True)
    phone = models.CharField(_('Номер телефона'), max_length=15, blank=True, null=True)
    tg = models.CharField(_('Telegram'), max_length=15, blank=True, null=True)
    linkedin_profile = models.CharField(_('Linkedin'), max_length=100, blank=True, null=True)
    reason = models.TextField(_('Почему хотите стать ментором?'), blank=True, null=True)
    photo = models.ImageField(_('Фотография'), upload_to='mentors/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('mentor_detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = _('Наставник')
        verbose_name_plural = _('Наставники')
        
        
