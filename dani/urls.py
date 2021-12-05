from django.urls import path
from dani import views


urlpatterns = [
    path('', views.dani_index, name='dani_index'),
]



