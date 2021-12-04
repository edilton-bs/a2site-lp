from django.urls import path
from website import views


urlpatterns = [
    path('', views.index, name='index'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('forum', views.forum, name='forum'),
    path('nota', views.nota, name='nota'),
    path('main', views.main, name='main'),
    path('profile', views.profile, name='profile'),
    #path('registrar', views.registrar, name="registrar")
]

