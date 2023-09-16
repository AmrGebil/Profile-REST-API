from django.urls import path
from .views import HelloApi
urlpatterns = [
   path('helloApi/',HelloApi.as_view() )
]
