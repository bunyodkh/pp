from django.urls import path

from .views import event_type_detail

app_name = 'events'

urlpatterns = [
    path('<slug:slug>', event_type_detail, name='eventtype-detail'),
]
