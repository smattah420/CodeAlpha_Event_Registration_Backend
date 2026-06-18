from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Event, Registration
from .serializers import (
    EventSerializer,
    RegistrationSerializer
)

class EventListView(
    generics.ListAPIView
):

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RegistrationCreateView(
    generics.CreateAPIView
):

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
