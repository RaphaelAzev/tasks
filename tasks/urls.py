from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alltasks', views.getall, name='getall'),
    path('posttask',views.post_task,name='post_task'),
]

