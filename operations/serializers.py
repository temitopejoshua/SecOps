from rest_framework import serializers
from . import models


class NativesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Natives
        fields = '__all__'


class CitizenSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Citizens
        fields = ('full_name',
                  'image',)


class ActivitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Activities
        fields = ('url',
                  'time_In',
                  'time_Out',
                  'elder',
                  'native',
                  'citizen',)


class EldersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Elders
        fields = (
            'url',
            'first_name',
            'last_name',
            'email',
            'staff_id',
            'phone_number',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'date_created',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username')
