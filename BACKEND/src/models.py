from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class RecycleType(models.Model):
    name = models.CharField('Наименование материала, например: Бумага', max_length=500, unique=True)
    # logo = models.ImageField('Картинка материала', upload_to='recycle_images', max_length=254)
    # color_hex = models.CharField('Цвет-индикатор этого материала, HEX (то есть выглядит как #2596be)\n'
    #                              'Указывается БЕЗ `#`!', max_length=6)

    def __str__(self):
        return self.name


class Project(models.Model):
    """ Проекты """
    name = models.CharField(max_length=500, unique=True)
    logo = models.ImageField('Логотип', upload_to='project_logos', max_length=254, null=True, blank=True)
    about = models.TextField('Описание')
    contact_url = models.URLField('Ссылка на сайт', null=True, blank=True)
    # contact_email = models.EmailField('Контактный email', null=True, blank=True)
    # contact_phone = models.CharField('Телефон для связи', max_length=11, null=True, blank=True)
    recycle_types = models.ManyToManyField(RecycleType, blank=True, verbose_name='Типы вторсырья, которые принимает организация')
    # admins = models.ManyToManyField(User, verbose_name='Список администраторов')
    lat = models.DecimalField('Координаты широты', max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField('Координаты долготы', max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.id, self.name)


class Event(models.Model):
    """ Мероприятия """
    banner = models.ImageField(upload_to='evnet_banners', max_length=1024)
    title = models.CharField("Название", max_length=150)
    sub_body = models.CharField("Краткое описание", max_length=500)
    about = models.TextField('О мероприятии')
    begin_date = models.DateField('Дата и время начала')
    # begin_time = models.TimeField('Время начала', null=True, blank=True)
    end_date = models.DateField('Дата и время предполагаемого окончания')
    # end_time = models.TimeField('Время предполагаемого окончания', null=True, blank=True)
    location = models.CharField('Адрес места проведения', max_length=1500, null=True, blank=True)
    # lat = models.DecimalField('Координаты широты', max_digits=9, decimal_places=6, null=True, blank=True)
    # lon = models.DecimalField('Координаты долготы', max_digits=9, decimal_places=6, null=True, blank=True)
    # organizer = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Организатор (Организация/проект)',
    #                               null=True, blank=True)
    is_top = models.BooleanField('Выводить в топ?', default=False)

    def __str__(self):
        return "%s - %s [%s]" % (self.id, self.title, self.begin_date)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто поставил оценку')
    score = models.FloatField("Оценка пользователя")
    event = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Какому мероприятию')

    class Meta:
        unique_together = ('user', 'event',)


class Advert(models.Model):
    """ Объявления """
    title = models.CharField("Заголовок", max_length=150)
    description = models.CharField("Краткое описание", max_length=300, null=True, blank=True)
    body = models.TextField("Текст объявления")
    photo = models.ImageField('Превью', upload_to='add_photos', max_length=254 * 2)
    # contacts = models.TextField("Контакты автора")
    # location = models.CharField("Адрес самовывоза", max_length=1500, null=True, blank=True)


class PickPoint(models.Model):
    """ Точки приема вторсырья на карте """
    name = models.CharField("Название организации", max_length=150)
    place = models.CharField("Адрес организации", max_length=1500, null=True, blank=True)
    lat = models.DecimalField('Координаты широты', max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField('Координаты широты', max_digits=9, decimal_places=6, null=True, blank=True)
    type = models.ManyToManyField(RecycleType, verbose_name='Типы материалов, которые принимает точка')
    about = models.TextField("Описание", null=True, blank=True)
