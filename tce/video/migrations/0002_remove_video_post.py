# Generated by Django 3.1.9 on 2022-01-20 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='post',
        ),
    ]
