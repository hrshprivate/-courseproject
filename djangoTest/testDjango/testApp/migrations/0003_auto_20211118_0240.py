# Generated by Django 3.2.9 on 2021-11-17 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testApp', '0002_auto_20211116_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='asd',
            field=models.CharField(max_length=200, null=True, verbose_name='NameAuthor'),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]