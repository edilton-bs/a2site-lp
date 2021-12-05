from django.urls import path
from caio import views


urlpatterns = [
    path('', views.index, name='index'),

]
