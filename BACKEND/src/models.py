from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class RecycleType(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """ Проекты """
    name = models.CharField(max_length=500, unique=True)
    logo = models.ImageField(upload_to='project_logos', max_length=254)
    about = models.TextField()
    contact_url = models.URLField()
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=11, null=True, blank=True)
    recycle_types = models.ManyToManyField(RecycleType, blank=True)
    admins = models.ManyToManyField(User)

    def __str__(self):
        return "%s %s" % (self.name, self.admins.all())


class Event(models.Model):
    """ Мероприятия """
    banner = models.ImageField(upload_to='evnet_banners', max_length=1024)
    about = models.TextField()
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=1500, null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    organizer = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.about, self.organizer.all())


class WallPost(models.Model):
    """ Посты (записи) """
    title = models.CharField("Заголовок", max_length=150)
    description = models.CharField("Краткое описание", max_length=300, null=True, blank=True)
    body = models.TextField("Текст поста")
    photo = models.ImageField(upload_to='wallpost_photos', max_length=254 * 2)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return "%s - [ %s ]" % (self.title, self.created.strftime('%Y.%m.%d'))


class ProjectMark(models.Model):
    """ Пользовательские оценки проектов """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField("Оценка пользователя")
    project = models.ForeignKey(Project, related_name="project_marks", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project',)

    def __str__(self):
        return "%s - %i - %s" % (self.user, self.score, self.project.name)


class EventMark(models.Model):
    """ Пользовательские оценки мероприятий """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField("Оценка пользователя")
    event = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'event',)


class Advert(models.Model):
    """ Объявления """
    title = models.CharField("Заголовок", max_length=150)
    description = models.CharField("Краткое описание", max_length=300, null=True, blank=True)
    body = models.TextField("Текст объявления")
    photo = models.ImageField(upload_to='add_photos', max_length=254 * 2)
    contacts = models.TextField("Контакты")
    location = models.CharField("Адрес самовывоза", max_length=1500, null=True, blank=True)


class PickPoint(models.Model):
    """ Точки приема вторсырья на карте """
    name = models.CharField("Название организации", max_length=150)
    place = models.CharField("Адрес организации", max_length=1500, null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    type = models.ManyToManyField(RecycleType)
    about = models.TextField("Название организации")
