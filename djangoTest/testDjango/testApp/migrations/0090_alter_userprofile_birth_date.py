# Generated by Django 3.2.9 on 2021-12-16 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0089_alter_userprofile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, max_length=8, null=True, verbose_name='Дата рождения'),
        ),
    ]
