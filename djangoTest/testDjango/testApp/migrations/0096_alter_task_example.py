# Generated by Django 3.2.9 on 2021-12-24 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0095_rename_second_name_userprofile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='example',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='example', to='testApp.example'),
        ),
    ]