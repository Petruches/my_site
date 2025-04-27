from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('me/', me),
    path('content/', content),
]
