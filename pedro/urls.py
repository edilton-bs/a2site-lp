from django.urls import path
from pedro import views


urlpatterns = [
    path('', views.index, name='index'),

]

