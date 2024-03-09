from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView



class ClientApiView(APIView):
    def get(self, requests, pk):
        client = Client.objects.get(pk=pk)
        client_lizer = ClientSerializer(client, partial=True)
        return Response({'client': client_lizer.data})
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'add_client': serializer.data})



# @csrf_exempt
# def client_by_pk(request, pk):
#     try:
#         client = Client.objects.get(pk=pk)
#     except Client.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = ClientSerializer(client)
#         return JsonResponse(serializer.data)
  
@csrf_exempt  
def add_client(request):
 
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


