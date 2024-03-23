from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='list'),
    path('update_task/<str:pk>', views.UpdateTask, name='update_task'),
    path('delete_task/<str:pk>', views.deleteTask, name='delete_task'),
    path('getTask/<str:pk>', views.getTask, name='task'),
    path('addTask/', views.addTask, name='new_task')
]