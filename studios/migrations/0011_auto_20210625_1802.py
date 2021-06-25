# Generated by Django 2.2.5 on 2021-06-25 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210623_0430'),
        ('studios', '0010_auto_20210623_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudioAbstractItem',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.TimeStampedModel')),
                ('name', models.CharField(max_length=80)),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='studios.Post'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='studio_photos'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('studioabstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='studios.StudioAbstractItem')),
            ],
            bases=('studios.studioabstractitem',),
        ),
    ]
