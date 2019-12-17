from django.shortcuts import render
from .models import Elders, Natives, Citizens, Activities, CustomUser
import operations.serializers as ss
from rest_framework import generics
import operations.models as om


# Create your views here.
class EldersList(generics.ListCreateAPIView):
    queryset = om.Elders.objects.all()
    serializer_class = ss.EldersSerializers
    name = "elders-list"


class ElderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = om.Elders.objects.all()
    serializer_class = ss.EldersSerializers
    name = "elders-detail"


class NativesList(generics.ListCreateAPIView):
    queryset = om.Natives.objects.all()
    serializer_class = ss.NativesSerializers
    name = "nativesList"


class NativesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = om.Natives.objects.all()
    serializer_class = ss.NativesSerializers
    name = "natives-detail"


class ActivitiesList(generics.ListCreateAPIView):
    queryset = om.Activities.objects.all()
    serializer_class = ss.ActivitiesSerializer
    name = 'activities-detail'


class ActivitiesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = om.Activities.objects.all()
    serializer_class = ss.ActivitiesSerializer
    name = 'activities-list'


class CitizensList(generics.ListCreateAPIView):
    queryset = om.Citizens.objects.all()
    serializer_class = ss.CitizenSerializers
    name = 'citizens-list'


class CitizensDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = om.Citizens.objects.all()
    serializer_class = ss.CitizenSerializers
    name = 'citizens-detail'


class UserList(generics.ListAPIView):
    queryset = om.CustomUser.objects.all()
    serializer_class = ss.UserSerializer
    name = "user-list"

