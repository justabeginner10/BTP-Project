# Generated by Django 4.0.1 on 2022-02-22 04:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0012_auto_20220201_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors.profile')),
                ('tags', models.ManyToManyField(blank=True, to='blogs.Tag')),
            ],
        ),
    ]
