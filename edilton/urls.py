from django.urls import path
from edilton import views


urlpatterns = [
    path('', views.index, name='index'),

]

