from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('delet/<int:task_id>/', views.delete_task, name='delete_task'),
path('complete/<int:task_id>/', views.complet_task, name='complete_task'),
]