# Generated by Django 2.2.5 on 2021-06-23 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0007_auto_20210623_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='artist',
        ),
    ]
