# Generated by Django 3.2.9 on 2021-11-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0010_auto_20211125_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='child_amount',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_merchant',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='postal_code_3',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='postal_code_4',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=150, null=True, verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.CharField(max_length=1, null=True, verbose_name='Пол'),
        ),
    ]
