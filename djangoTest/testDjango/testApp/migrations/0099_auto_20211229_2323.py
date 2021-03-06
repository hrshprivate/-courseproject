# Generated by Django 3.2.9 on 2021-12-29 23:23

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0098_alter_task_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[500, 300], upload_to='get_image_path', verbose_name='Картинка'),
        ),
    ]
