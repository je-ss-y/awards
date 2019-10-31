from rest_framework import serializers
from .models import *

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snap
        fields = ('image', 'photoname', 'description')


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'profilepicture')

