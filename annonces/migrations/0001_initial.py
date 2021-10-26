# Generated by Django 3.2.8 on 2021-10-21 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, null=True)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='annonces.category')),
            ],
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('price', models.PositiveIntegerField(default=0)),
                ('condition', models.CharField(choices=[('NE', 'Neuf avec étiquettes'), ('NS', 'Neuf sans étiquettes'), ('TE', 'Très bon état'), ('BE', 'Bon état'), ('ST', 'Satisfaisant')], max_length=100)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('give', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annonces', to='annonces.category')),
                ('color', models.ManyToManyField(blank=True, related_name='annonces', to='annonces.Color')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='annonces.annonce')),
                ('size', models.ManyToManyField(blank=True, related_name='annonces', to='annonces.Size')),
                ('tag', models.ManyToManyField(blank=True, related_name='annonces', to='annonces.Tag')),
            ],
        ),
    ]
