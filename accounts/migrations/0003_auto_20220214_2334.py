# Generated by Django 3.2.5 on 2022-02-14 20:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_user_education_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='hub_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact_address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact_phone_number',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_personal_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
