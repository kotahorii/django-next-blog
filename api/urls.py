from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from api.views import TaskViewSet, TaskListView, TaskRetrieveView,\
    CreateUserView, PostListView, PostRetrieveView

router