from .models import Assist
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our AssistSerializer
class AssistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Assist
        # the fields that should be included in the serialized output
        fields = ['id', 'project', 'manufacture', 'address', 'due', 'details']