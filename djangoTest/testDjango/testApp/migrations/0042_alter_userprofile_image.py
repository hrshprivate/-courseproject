# Generated by Django 3.2.9 on 2021-11-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0041_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/media', verbose_name='Картинка'),
        ),
    ]
