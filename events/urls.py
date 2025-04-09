from django.urls import path

from .views import event_list, event_registration

app_name = 'events'

urlpatterns = [
    path('', event_list, name='event-list'),
    path('<str:event_number>/registration', event_registration, name='event-registration'),
]
