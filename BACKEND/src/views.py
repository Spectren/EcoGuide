from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from src.serializers import UserSerializer, GroupSerializer, RecycleTypeSerializer, ProjectSerializer, EventSerializer, \
    WallPostSerializer, PickPointSerializer, AdvertSerializer
from src.models import RecycleType, Project, Event, WallPost, PickPoint, Advert


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class RecycleTypeView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RecycleTypeSerializer

    def get_queryset(self):
        return RecycleType.objects.all()

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class ProjectView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class EventView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all().order_by('-is_top', '-begin_date')

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class EventTopView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(is_top=True).order_by('-begin_date')

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class WallPostView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = WallPostSerializer

    def get_queryset(self):
        return WallPost.objects.all()

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class AdvertView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = AdvertSerializer

    def get_queryset(self):
        return Advert.objects.all()

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)


class PickPointView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = PickPointSerializer

    def get_queryset(self):
        return PickPoint.objects.all()

    def get_paginated_response(self, data):
        """ Избавляемся от пагинации в ответе """
        return Response(data)
