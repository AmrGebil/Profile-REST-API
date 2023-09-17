from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HelloApi,HelloViewSet

router=DefaultRouter()

router.register('hello-viewset',HelloViewSet,basename='hello-viewset')

urlpatterns = [
   path('helloApi/',HelloApi.as_view() ),
   path('',include(router.urls) )
]
