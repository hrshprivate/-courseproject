# Generated by Django 3.2.9 on 2021-11-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0021_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Name',
            field=models.CharField(max_length=150, null=True, verbose_name='Адресс'),
        ),
    ]