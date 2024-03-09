from django.contrib.auth.models import User
from rest_framework import serializers
from box.models import *



class ClientSerializer(serializers.Serializer):
    id_by_tg = serializers.IntegerField()
    name_tg = serializers.CharField()
    name = serializers.CharField()
    phone_number = serializers.IntegerField()
    email = serializers.EmailField()
    language = serializers.CharField()
    country = serializers.CharField()
    code_warification = serializers.IntegerField()

    def create(self, validated_data):
        return Client.objects.create(**validated_data)


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

