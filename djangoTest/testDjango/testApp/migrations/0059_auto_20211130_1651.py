# Generated by Django 3.2.9 on 2021-11-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0058_auto_20211130_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='Введите мыло:'),
        ),
    ]
