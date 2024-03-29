# Generated by Django 3.2.5 on 2022-02-14 21:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220214_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+251935629442', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
