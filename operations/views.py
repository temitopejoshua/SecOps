from rest_framework.response import Response
from rest_framework.reverse import reverse

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


class ApiRoot(generics.ListAPIView):
    name = 'Welcome to SecOps-API'

    def get(self, request, *args, **kwargs):
        return Response({
            'elder-list': reverse(EldersList.name, request=request),
            'natives-list': reverse(NativesList.name, request=request),
            'activities-list': reverse(ActivitiesList.name, request=request),
            'citizen-list': reverse(CitizensList.name, request=request),
            'api-documentation-local': 'http://127.0.0.1:8000/redoc/',
            'api-documentation-online': 'https://secops-api.herokuapp.com/redoc/'

        })
