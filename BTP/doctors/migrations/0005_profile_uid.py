# Generated by Django 3.2.8 on 2022-01-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_remove_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Uid',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
