from django.contrib.auth.models import User
from rest_framework import serializers
from box.models import *



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
    id_box = serializers.IntegerField
    name = serializers.CharField()
    description = serializers.DictField()
    summ = serializers.DecimalField(max_digits=6, decimal_places=2)
    choice = serializers.IntegerField()
    type_distrybushin = serializers.CharField()
    summ_now = serializers.CharField()
    distrybushim_now = serializers.CharField()
    status = serializers.BooleanField(default=True)

