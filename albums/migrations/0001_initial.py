# Generated by Django 3.1.3 on 2020-11-30 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=60)),
                ('release_date', models.DateField()),
                ('fave', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=60)),
                ('artist_image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_title', models.CharField(max_length=200)),
                ('track_length', models.CharField(max_length=60)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.albums')),
            ],
        ),
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.tracks')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.artists'),
        ),
    ]
