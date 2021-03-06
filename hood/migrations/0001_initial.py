# Generated by Django 4.0.4 on 2022-04-20 22:02

import cloudinary.models
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
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhoodName', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hoodMember', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('postBody', models.TextField()),
                ('postImage', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicesName', models.CharField(max_length=200)),
                ('servicePhone', models.CharField(max_length=255)),
                ('serviceEmail', models.EmailField(max_length=200)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(max_length=100)),
                ('businessPhone', models.CharField(max_length=255, null=True)),
                ('businessEmail', models.EmailField(max_length=254, null=True)),
                ('businessOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood')),
            ],
        ),
    ]
