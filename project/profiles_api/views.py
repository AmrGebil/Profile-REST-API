from django.shortcuts import render

from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
# Create your views here.

class HelloApi(APIView):
    """ teat Api View"""
    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'hello','apiView':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serialiser=HelloSerializer(data=request.data)
        if serialiser.is_valid():
            name=serialiser.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)
        



