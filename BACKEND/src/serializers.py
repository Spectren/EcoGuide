from django.contrib.auth.models import User, Group
from .models import Project, RecycleType, Event, ProjectMark, WallPost, Advert, PickPoint
from rest_framework import serializers
from django.db.models import Avg


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RecycleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecycleType
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    logo = serializers.ImageField()
    about = serializers.CharField()
    contact_url = serializers.URLField()
    # contact_email = serializers.EmailField()
    # contact_phone = serializers.CharField()
    # recycle_types = RecycleTypeSerializer(many=True)
    recycles = serializers.SerializerMethodField('get_recycle_types')
    # admins = UserSerializer(many=True)
    mark = serializers.SerializerMethodField('count_mark')
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    lon = serializers.DecimalField(max_digits=9, decimal_places=6)

    def count_mark(self, project):
        """ Считаем среднюю оценку проекта """
        return project.project_marks.all().aggregate(Avg('score')).get('score__avg')

    def get_recycle_types(self, project):
        return project.recycle_types.all().values_list('name', flat=True)

    class Meta:
        model = Project
        # fields = ['id', 'name', 'logo', 'about', 'contact_url', 'contact_email', 'contact_phone', 'recycle_types',
        #           'admins', 'mark']
        fields = ['id', 'name', 'logo', 'about', 'contact_url', 'mark', 'lat', 'lon', 'recycles']


class EventSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField()
    title = serializers.CharField()
    sub_body = serializers.CharField()
    about = serializers.CharField()
    begin_date = serializers.DateField()
    # begin_time = serializers.TimeField()
    end_date = serializers.DateField()
    # end_time = serializers.TimeField()
    location = serializers.CharField()
    is_top = serializers.BooleanField()

    # lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    # lon = serializers.DecimalField(max_digits=9, decimal_places=6)
    # organizer = ProjectSerializer(read_only=True)

    class Meta:
        model = Event
        # fields = ['id', 'banner', 'about', 'begin_date', 'end_date', 'location', 'lat', 'lon', 'organizer']
        # fields = '__all__'
        fields = ['id', 'banner', 'title', 'about', 'sub_body', 'begin_date', 'end_date', 'location', 'is_top']


class WallPostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    photo = serializers.ImageField()
    likes = serializers.SerializerMethodField('count_likes')
    user_liked = serializers.SerializerMethodField()  # Лайкнул ли указанный юзер пост

    def count_likes(self, wallPost):
        """ Считаем количество лайков """
        return wallPost.likes.count()

    def get_user_liked(self, wallPost):
        """ Лайкнул ли указанный юзер пост """
        user = self.context.get('request').user

        # FIXME: Исправить на правильную конструкцию с подзапросом
        if user in wallPost.likes.all():
            return True
        return False

        # Примерно такую:
        # if wallPost.likes.filter(post_likes=user.id).exists():
        #     return False
        # return True

    class Meta:
        model = WallPost
        fields = ('title', 'description', 'body', 'photo', 'likes', 'user_liked')


class AdvertSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    photo = serializers.ImageField()
    # contacts = serializers.CharField()
    # location = serializers.CharField()

    class Meta:
        model = Advert
        fields = '__all__'


class PickPointSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    place = serializers.CharField()
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    lon = serializers.DecimalField(max_digits=9, decimal_places=6)
    type = RecycleTypeSerializer()
    about = serializers.CharField()

    class Meta:
        model = PickPoint
        fields = '__all__'
