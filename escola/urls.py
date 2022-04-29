from django.urls import path 
from .views import *

from . import views


urlpatterns = [
    path('', views.aulas, name='aulas'),
    path('alunos/<int:id>/', views.alunos, name='alunos'),


]