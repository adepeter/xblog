# Generated by Django 3.0.7 on 2020-06-23 16:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import xblogapps.cores.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=xblogapps.cores.utils.ImageHandler.upload_handler)),
                ('slug', models.SlugField(blank=True)),
                ('content', models.TextField(unique_for_date='published')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_locked', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_hidden', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blogs.Article', verbose_name='article')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blogs.Post')),
            ],
        ),
    ]
