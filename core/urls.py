from django.conf.urls import url, include
from rest_framework import routers
from .views.user_view import UserViewSet
from .views.person_view import PersonViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
