from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
from django.utils.translation import gettext as _
from PIL import Image
from django.utils.text import slugify


from core.utils import rename_uploaded_image


class EventType(models.Model):
    name = models.CharField(_('Название'), max_length=200, blank=False, null=False)
    image = models.ImageField(_('Изображение'), upload_to=rename_uploaded_image, blank=True, null=True)
    description = models.TextField(_('Описание'), blank=False, null=False, default='Event description')

    slug = models.SlugField(_('Slug'), max_length=200, unique=True, blank=True)  # Add slug field

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_active_event(self):
        return self.event_set.filter(active=True).first()
    
    def get_absolute_url(self):
        return reverse('events:eventtype-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Тип мероприятия')
        verbose_name_plural = _('Типы мероприятий')


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            # Ensure the slug is unique
            while EventType.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        
        super().save(*args, **kwargs)

        # Optimize the image
        if self.image:
            image_path = self.image.path  # Get the file path of the uploaded image
            image = Image.open(image_path)

            # Resize the image if it exceeds the desired dimensions
            max_width, max_height = 800, 800  # Set the maximum dimensions
            if image.width > max_width or image.height > max_height:
                image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
                image.save(image_path, optimize=True, quality=85)  # Save the optimized image


class Event(models.Model):
    event_type = models.ForeignKey('EventType', on_delete=models.CASCADE, related_name='events', verbose_name=_('Тип мероприятия'), blank=True, null=True)

    name = models.CharField(_('Название'), max_length=200, blank=False, null=False, default='Название мероприятия')
    emphasis_to_name = models.CharField(_('Акцент к названию'), max_length=10, blank=False, null=False, default='Event')
    location = models.CharField(_('Место проведения'), max_length=200, blank=False, null=False)
    planned_date = models.DateTimeField(_('Дата проведения'), blank=True, null=True)
    registration_deadline = models.DateTimeField(_('Дата окончания регистрации'), blank=False, null=False)

    event_number = models.CharField(max_length=8, unique=True, blank=True, editable=False)
    active = models.BooleanField(_('Активно'), default=False)
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
        hero_image = self.event_photos.filter(hero_image=True).first()
        return hero_image.photo.url if hero_image else None


    def save(self, *args, **kwargs):
        if self.active:
            Event.objects.filter(active=True).exclude(id=self.id).update(active=False)
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
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event_photos', verbose_name=_('Мероприятие'))
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

    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='participants')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Участник')
        verbose_name_plural = _('Участники')



class Achievement(models.Model):
    event = models.ForeignKey('EventType', on_delete=models.CASCADE, related_name='achievements', verbose_name=_('Тип мероприятия'), blank=True, null=True)
    value = models.CharField(_('Значение'), max_length=20, blank=True, null=True)
    title = models.CharField(_('Название'), max_length=20, blank=True, null=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.value} {self.title} {self.event}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Достижение')
        verbose_name_plural = _('Достижения')


class EventWinner(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event_winners', verbose_name=_('Мероприятие'), blank=True, null=True)
    name = models.CharField(_('Название стартапа'), max_length=100, blank=True, null=True)
    description = models.TextField(_('Описание стартапа'), max_length=500, blank=True, null=True)
    logo = models.ImageField(_('Логотип стартапа'), upload_to=rename_uploaded_image, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Победитель')
        verbose_name_plural = _('Победители')

    def __str__(self):
        return f'{self.name} {self.event}'