# Generated by Django 3.2.9 on 2021-11-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0039_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/testApp/jpg', verbose_name='Картинка'),
        ),
    ]
