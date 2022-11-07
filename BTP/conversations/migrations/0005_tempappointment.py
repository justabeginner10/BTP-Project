# Generated by Django 4.0.1 on 2022-11-06 05:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('doctors', '0021_alter_profile_statemedicalcouncil'),
        ('conversations', '0004_appointment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempAppointment',
            fields=[
                ('tempAppointmentID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recieverProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TempRecieverInConversation', to='clients.clientprofile')),
                ('senderProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TempSenderInConversation', to='doctors.profile')),
            ],
        ),
    ]
