# Generated by Django 3.2.9 on 2021-11-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0051_alter_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tg',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vk',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Вконтакте'),
        ),
    ]
