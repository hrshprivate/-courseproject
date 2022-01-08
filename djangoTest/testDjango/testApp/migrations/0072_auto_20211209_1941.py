# Generated by Django 3.2.9 on 2021-12-09 19:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testApp', '0071_auto_20211209_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ManyToManyField(max_length=1000000, related_name='pisun', to=settings.AUTH_USER_MODEL),
        ),
    ]
