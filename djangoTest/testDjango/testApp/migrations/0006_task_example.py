# Generated by Django 3.2.9 on 2021-11-17 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='example',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testApp.example'),
            preserve_default=False,
        ),
    ]
