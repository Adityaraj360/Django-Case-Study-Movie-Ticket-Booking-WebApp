# Generated by Django 4.1.6 on 2023-02-10 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0010_seats_shows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seats',
            name='S_No',
        ),
    ]