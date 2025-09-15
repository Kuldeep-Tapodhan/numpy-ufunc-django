from django.urls import path
from . import views

urlpatterns = [
    path('', views.ufunc_view, name='ufunc_view'),
]