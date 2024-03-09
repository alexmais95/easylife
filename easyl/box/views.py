from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def client_list(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return JsonResponse(serializer.data)




