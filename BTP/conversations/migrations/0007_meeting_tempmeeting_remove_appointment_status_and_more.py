# Generated by Django 4.0.1 on 2022-11-06 05:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('doctors', '0021_alter_profile_statemedicalcouncil'),
        ('conversations', '0006_alter_appointment_appointmentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('appointmentID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('appointmentLink', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('clientProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ClientForMeeting', to='clients.clientprofile')),
                ('doctorProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DoctorForMeeting', to='doctors.profile')),
            ],
        ),
        migrations.CreateModel(
            name='TempMeeting',
            fields=[
                ('tempAppointmentID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('clientProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TempClientInMeeting', to='clients.clientprofile')),
                ('doctorProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TempDoctorInMeeting', to='doctors.profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.DeleteModel(
            name='TempAppointment',
        ),
    ]
