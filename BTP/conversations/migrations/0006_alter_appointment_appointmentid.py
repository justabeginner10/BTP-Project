# Generated by Django 4.0.1 on 2022-11-06 05:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0005_tempappointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentID',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
