# Generated by Django 3.2.9 on 2021-11-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='time_create',
            field=models.DateField(auto_now=True),
        ),
    ]
