# Generated by Django 3.2.9 on 2021-11-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0056_alter_userprofile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, default='%Y-%m-01', null=True, verbose_name='Дата рождения'),
        ),
    ]
