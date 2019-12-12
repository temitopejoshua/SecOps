from django.shortcuts import render
from .models import Elders, Natives, Citizens, Activities, CustomUser
from .serializers import EldersSerializers, NativesSerializers, CitizenSerializers, ActivitiesSerializer, UserSerializer
from rest_framework import generics


# Create your views here.
class EldersList(generics.ListCreateAPIView):
    queryset = Elders.objects.all()
    serializer_class = EldersSerializers
    name = "elders-list"


class ElderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elders.objects.all()
    serializer_class = EldersSerializers
    name = "elders-detail"


class NativesList(generics.ListCreateAPIView):
    queryset = Natives.objects.all()
    serializer_class = NativesSerializers
    name = "nativesList"


class NativesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Natives.objects.all()
    serializer_class = NativesSerializers
    name = "natives-detail"


class ActivitiesList(generics.ListCreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    name = 'activities-detail'


class ActivitiesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    name = 'activities-list'


class CitizensList(generics.ListCreateAPIView):
    queryset = Citizens.objects.all()
    serializer_class = CitizenSerializers
    name = 'citizens-list'


class CitizensDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizens.objects.all()
    serializer_class = CitizenSerializers
    name = 'citizens-detail'


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    name = "user-list"
