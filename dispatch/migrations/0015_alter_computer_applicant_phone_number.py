# Generated by Django 3.2.5 on 2022-03-13 19:30

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0014_alter_computer_request_memory_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_applicant',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]