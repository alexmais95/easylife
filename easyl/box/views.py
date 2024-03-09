from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend



#Повертає інформацію про клієнта та має функціонал додавання клієнта.
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
    
 
#Інформація про бокси, містить методи Put, get, post 
class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


#Містить фільтр який відображає які бокси належать юзеру.
class UserBoxlist(generics.ListAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user']

#Містить фільтр який відображає операції юзера
class OperationVievList(generics.ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['id_by_tg']

#Містить фільтр який відображає кількість монет юзера
class CoinVievList(generics.ListAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user']
   
    




