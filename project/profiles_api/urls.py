from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HelloApi,HelloViewSet,UserLoginApiView,UserProfileViewSet

router=DefaultRouter()

router.register('hello-viewset',HelloViewSet,basename='hello-viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
   path('helloApi/',HelloApi.as_view() ),
   path('login/', UserLoginApiView.as_view()),
   path('',include(router.urls) )
]
