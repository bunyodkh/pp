from django.urls import path
from django.views.generic.base import RedirectView

from .views import event_type_detail

app_name = 'events'

urlpatterns = [
    path('', RedirectView.as_view(url='/ru/#events', permanent=False), name='events-redirect'),
    path('<slug:slug>', event_type_detail, name='eventtype-detail'),
]
