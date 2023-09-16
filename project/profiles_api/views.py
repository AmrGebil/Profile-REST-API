from django.shortcuts import render

from  rest_framework.views import APIView
from rest_framework.response import Response

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


