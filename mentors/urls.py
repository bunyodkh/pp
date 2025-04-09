from django.urls import path

from .views import (
    mentor_list,
    mentor_add,
)

app_name = 'mentors'

urlpatterns = [
    path('', mentor_list, name='mentor-list'),
    path('become-a-mentor/', mentor_add, name='mentor-add'),
]
