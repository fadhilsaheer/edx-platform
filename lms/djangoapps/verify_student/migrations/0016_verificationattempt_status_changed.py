# Generated by Django 4.2.15 on 2024-09-19 16:17

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('verify_student', '0015_verificationattempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationattempt',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed'),
        ),
    ]
