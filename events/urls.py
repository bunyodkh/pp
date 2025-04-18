from django.urls import path

from .views import event_detail, event_registration

app_name = 'events'

urlpatterns = [
    path('<str:event_number>', event_detail, name='event-registration'),
    path('<str:event_number>/registration', event_registration, name='event-registration'),
]
