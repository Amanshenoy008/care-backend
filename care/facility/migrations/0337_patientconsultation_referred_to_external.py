# Generated by Django 2.2.11 on 2023-03-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0336_auto_20230222_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientconsultation',
            name='referred_to_external',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
