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
    class Meta:
        model = Box
        fields = '__all__'


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


