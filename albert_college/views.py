from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Parent, Student, ClassRoom
from .serializer import ParentSerializers, StudentSerializers, ClassRoomSerializers
# Create your views here.



class StudentViewset(ListModelMixin, CreateModelMixin, GenericViewSet):
      queryset = Student.objects.all()
      serializer_class = StudentSerializers

@api_view(['GET', 'POST'])
@csrf_exempt
def classroom_list(request):
      if request.method == "GET":
            classrooms = ClassRoom.objects.all()
            serializer = ClassRoomSerializers(classrooms, many=True)
            return Response(serializer.data)
      elif request.method == 'POST':
            serializer = ClassRoomSerializers(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
      
@api_view(['GET','PUT', 'DELETE'])
@csrf_exempt
def classroom_detail(request, id):
      print(request.method)
      classrooms = get_object_or_404(ClassRoom, pk=id)
      if request.method == 'GET':
            serializer = ClassRoomSerializers(classrooms)
            return Response(serializer.data)
      elif request.method == 'PUT':
            serializer = ClassRoomSerializers(classrooms, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
      elif request.method == "DELETE":
            classrooms.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET', 'POST'])
@csrf_exempt
def parent_list(request):
      if request.method == 'GET':
            parents = Parent.objects.all()
            serializer = ParentSerializers(parents, many=True)
            return Response(serializer.data)
      elif request.method == 'POST':
            serializer = ParentSerializers(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
      
@api_view(['GET','PATCH', 'DELETE'])
@csrf_exempt
def parent_detail(request, id):
      parents = get_object_or_404(Parent, pk=id)
      print(request.method)
      if request.method == 'GET':
            serializer = ParentSerializers(parents)
            return Response(serializer.data)
      elif request.method == 'PATCH':
            serializer = ParentSerializers(parents, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            
