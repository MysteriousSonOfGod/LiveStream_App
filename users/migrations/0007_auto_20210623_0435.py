# Generated by Django 2.2.5 on 2021-06-22 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0006_remove_channel_artist'),
        ('users', '0006_user_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='genre',
        ),
        migrations.AddField(
            model_name='user',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='channels.Channel'),
        ),
    ]
