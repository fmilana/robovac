# encoding: utf-8

from django.urls import path
from .views import webhook_view

urlpatterns = [
    path('', webhook_view),
]
