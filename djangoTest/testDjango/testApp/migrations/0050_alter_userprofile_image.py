# Generated by Django 3.2.9 on 2021-11-29 17:32

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0049_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=75, size=[500, 300], upload_to='', verbose_name='Картинка'),
        ),
    ]
