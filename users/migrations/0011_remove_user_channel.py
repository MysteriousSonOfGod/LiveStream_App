# Generated by Django 2.2.5 on 2021-06-23 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210623_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='channel',
        ),
    ]
