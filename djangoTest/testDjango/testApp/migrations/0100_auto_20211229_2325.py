# Generated by Django 3.2.9 on 2021-12-29 23:25

from django.db import migrations
import django_resized.forms
import testApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0099_auto_20211229_2323'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[500, 300], upload_to=testApp.models.UserProfile.get_image_path, verbose_name='Картинка'),
        ),
    ]