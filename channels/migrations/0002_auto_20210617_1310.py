# Generated by Django 2.2.5 on 2021-06-17 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractItem',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.TimeStampedModel')),
                ('name', models.CharField(max_length=80)),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.AddField(
            model_name='channel',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='channel',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=746, multiple=True),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='channels.AbstractItem')),
            ],
            bases=('channels.abstractitem',),
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='channels.AbstractItem')),
            ],
            bases=('channels.abstractitem',),
        ),
        migrations.AddField(
            model_name='channel',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='channels', to='channels.Genre'),
        ),
        migrations.AddField(
            model_name='channel',
            name='resolution',
            field=models.ManyToManyField(related_name='channels', to='channels.Resolution'),
        ),
    ]