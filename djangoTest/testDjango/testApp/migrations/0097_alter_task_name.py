# Generated by Django 3.2.9 on 2021-12-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0096_alter_task_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='NameAuthor'),
        ),
    ]
