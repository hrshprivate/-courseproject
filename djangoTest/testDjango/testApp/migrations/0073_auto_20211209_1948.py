# Generated by Django 3.2.9 on 2021-12-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0072_auto_20211209_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000, null=True),
        ),
    ]
