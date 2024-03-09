from .models import *
from .serializers import *
from rest_framework.response import Response
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






