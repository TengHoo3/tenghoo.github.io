from django.contrib import admin
from django.urls import path, include
from . import views
from .views import predict

app_name = 'digitrecog'

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('api/predict/', predict)
]