from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from pytils import translit


class Example(models.Model):

    class Meta:
        verbose_name = 'Ключ'
        verbose_name_plural = 'Ключи'

    Name = models.CharField('NameKey', max_length=200, null=True, unique=True)


    def __str__(self):
         return self.Name


class Task(models.Model):

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    title = models.CharField('Name', max_length=200)
    task = models.TextField('Desc:')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="au")
    name = models.CharField('NameAuthor', max_length=200, null=True, blank=True)
    example = models.ForeignKey(Example, on_delete=models.CASCADE, null=True, related_name="example")

    def __str__(self):
         return self.title


class UserProfile(models.Model):

    MALE_CHOICES = (
        ('М', 'М'),
        ('Ж', 'Ж'),
    )
    def get_image_path(self, filename):
        path = ''.join(["pictures/", translit.slugify(filename)])
        return path

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField('Имя', max_length=150, null=True)
    last_name = models.CharField('Фамилия', max_length=150, null=True)
    birth_date = models.CharField('Дата рождения', null=True, blank=True, max_length=12)
    data = models.DateField(null=True, blank=True, max_length=50)
    genre = models.CharField('Пол', max_length=1, null=False, choices=MALE_CHOICES)
    address = models.CharField('Адресс', max_length=150, null=True, blank=True)
    age = models.PositiveIntegerField('Возраст', null=True, max_length=2)
    email = models.EmailField('Введите мыло:', max_length=100, null=True)
    image = ResizedImageField(size=[500, 300], quality=100, blank=True, upload_to=get_image_path, verbose_name='Картинка')
    vk = models.URLField('Вконтакте', max_length=150, null=True, blank=True)
    tg = models.URLField('Телеграм', max_length=150, null=True, blank=True)

    def bit(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
        bit.short_description = 'Картинка'
        bit.allow_tags = True

    def __str__(self):
         return str(self.user)


class Room(models.Model):
    name = models.CharField(max_length=1000, null=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="test")
    author = models.ManyToManyField(User, related_name="author", blank=True)

    def __str__(self):
         return self.name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now=True, blank=True)
    user = models.CharField(max_length=1000000, null=True)
    room = models.CharField(max_length=1000000)

    def __str__(self):
         return self.user





