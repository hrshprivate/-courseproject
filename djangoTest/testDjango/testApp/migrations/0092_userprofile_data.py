# Generated by Django 3.2.9 on 2021-12-16 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0091_alter_userprofile_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='data',
            field=models.DateField(blank=True, max_length=50, null=True),
        ),
    ]
