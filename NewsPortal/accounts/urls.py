from django.urls import path
from .views import SighUp

urlpatterns = [
    path('sighup', SighUp.as_view(), name='sighup'),
]