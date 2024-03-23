from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from rest_framework.decorators import api_view
from .serializers import ModelSerializer
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.response import Response


@api_view(['GET'])
def getTask(request, pk):
   try:
      activity= Task.objects.get(id=pk)
      converted=TaskSerializer(activity)
      return Response(converted.data)
   except:
      return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
def addTask(request):
   try:
      if request.method=='POST':
         Serialized=TaskSerializer(data=request.data)
         if Serialized.is_valid():
            Serialized.save()
         return Response(status=status.HTTP_201_CREATED)
   except:
      return Response(status=status.HTTP_400_BAD_REQUEST)
   try:
        task = Task.objects.all()
        
   except:
       return Response(status=status.HTTP_404_NOT_FOUND)

   return Response(request.data,status=status.HTTP_200_OK)

   
def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method=='POST':
       form=TaskForm(request.POST)
       if form.is_valid():
        form.save()
       return redirect('/')
    context={'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html',context)


def UpdateTask(request, pk):
   task=Task.objects.get(id=pk)
   form=TaskForm(instance=task)
   context={'form':form}
   if request.method=='POST':
      form=TaskForm(request.POST, instance=task)
      if form.is_valid():
         form.save()
         return redirect('/')
   return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
   item=Task.objects.get(id=pk)
   context={'item':item}
   if request.method == 'POST':
      item.delete()
      return redirect('/')
   return render(request, 'tasks/delete.html', context)
