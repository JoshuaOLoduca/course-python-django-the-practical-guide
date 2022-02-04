from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('january', views.index),
    path('february', views.index2),
]
