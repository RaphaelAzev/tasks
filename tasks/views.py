from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from .models import TaskSerializer
from .models import Task
from rest_framework.parsers import JSONParser

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def getall(request):
    tasks = Task.objects.all()
    json = serializers.serialize("json", tasks)
    return HttpResponse(json, content_type="application/json")


@api_view(["POST"])
def post_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)