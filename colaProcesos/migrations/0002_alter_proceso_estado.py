# Generated by Django 3.2.12 on 2022-09-29 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaProcesos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='estado',
            field=models.SmallIntegerField(default=('En espera',)),
        ),
    ]
