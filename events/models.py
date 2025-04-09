from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
from django.utils.translation import gettext as _

from core.utils import rename_uploaded_image

class Event(models.Model):
    name = models.CharField(_('Название'), max_length=200, blank=False, null=False)
    emphasis_to_name = models.CharField(_('Акцент к названию'), max_length=10, blank=False, null=False, default='Event')
    description = models.TextField(_('Описание'), blank=False, null=False)
    location = models.CharField(_('Место проведения'), max_length=200, blank=False, null=False)
    planned_date = models.DateTimeField(_('Дата проведения'), blank=True, null=True)
    registration_deadline = models.DateTimeField(_('Дата окончания регистрации'), blank=False, null=False)

    event_number = models.CharField(max_length=8, unique=True, blank=True, editable=False)
    active = models.BooleanField(_('Активно'), default=True)
    show_on_main = models.BooleanField(_('Показывать на главной'), default=False)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_registration_open(self):
        return timezone.now() <= self.registration_deadline
    
    def get_year(self):
        return self.planned_date.year if self.planned_date else None

    def get_hero_image(self):
        hero_image = self.eventphoto_set.filter(hero_image=True).first()
        return hero_image.photo.url if hero_image else None
    
    
    def get_absolute_url(self):
        return reverse('events:event-registration', kwargs={'event_number': self.event_number})


    def save(self, *args, **kwargs):
        if not self.event_number:
            self.event_number = str(uuid.uuid4().hex[:8])
        if self.show_on_main:
            Event.objects.filter(show_on_main=True).update(show_on_main=False)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')



class EventPhoto(models.Model):
    event = models.ForeignKey('Event', on_delete=models.DO_NOTHING)
    photo = models.ImageField(_('Фотография мероприятия'), upload_to=rename_uploaded_image, blank=False, null=False)
    hero_image = models.BooleanField(_('Главное изображение'), default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event.name} - {self.photo}"

    def save(self, *args, **kwargs):
        if self.hero_image:
            EventPhoto.objects.filter(event=self.event, hero_image=True).update(hero_image=False)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Фотография мероприятия')
        verbose_name_plural = _('Фотографии мероприятий')



class Participant(models.Model):
    full_name = models.CharField(_('Полное имя'), max_length=100, blank=True, null=True)
    institution = models.CharField(_('Учебное заведение'), max_length=100, blank=True, null=True)
    tg = models.CharField(_('Telegram'), max_length=100, blank=True, null=True)
    email = models.EmailField(_('Электронная почта'), max_length=100, blank=True, null=True)

    project = models.CharField(_('Название проекта'), max_length=100, blank=True, null=True)
    role = models.CharField(_('Ваша роль в проекте'), max_length=100, blank=True, null=True)

    link = models.CharField(_('Ссылка на презентацию'), max_length=500, blank=True, null=True)
    description = models.TextField(_('Описание проекта'), max_length=500, blank=True, null=True)

    event = models.ForeignKey('Event', on_delete=models.DO_NOTHING, related_name='participants')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Участник')
        verbose_name_plural = _('Участники')
