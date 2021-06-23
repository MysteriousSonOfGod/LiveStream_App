# Generated by Django 2.2.5 on 2021-06-23 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0007_auto_20210623_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studio',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='studio_board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='studios.Post'),
        ),
    ]
