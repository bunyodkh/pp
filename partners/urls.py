from django.urls import path

from .views import partner_add

app_name = 'partners'

urlpatterns = [
    path('become-a-partner/', partner_add, name='partner-add'),
]
