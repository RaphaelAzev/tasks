from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alltasks', views.getall, name='See_tasks'),
    path('posttask',views.post_task,name='Add_task')
]

