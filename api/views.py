from django.db.models import query
from rest_framework import generics, viewsets
from rest_framework import permissions
from .serializers import TaskSerializer, PostSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from .models import Task, Post


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permissions_classes = (AllowAny,)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (AllowAny,)


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_class = (AllowAny,)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permissions_classes = (AllowAny,)


class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer()
    permissions_classes = (AllowAny,)
