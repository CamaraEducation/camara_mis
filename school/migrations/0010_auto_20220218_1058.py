# Generated by Django 3.2.5 on 2022-02-18 07:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_alter_school_district_or_woreda_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone_number_1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='school',
            name='phone_number_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None),
        ),
    ]