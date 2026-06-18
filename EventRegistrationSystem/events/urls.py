from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        EventListView.as_view()
    ),

    path(
        'events/',
        EventListView.as_view()
    ),

    path(
        'register/',
        RegistrationCreateView.as_view()
    ),
]