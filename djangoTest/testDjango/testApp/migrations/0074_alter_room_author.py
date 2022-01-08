# Generated by Django 3.2.9 on 2021-12-09 19:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testApp', '0073_auto_20211209_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='author',
            field=models.ManyToManyField(limit_choices_to=django.contrib.auth.models.User, null=True, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]