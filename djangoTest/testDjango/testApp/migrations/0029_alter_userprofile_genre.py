# Generated by Django 3.2.9 on 2021-11-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0028_alter_userprofile_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.CharField(max_length=1, verbose_name='Пол'),
        ),
    ]
