# Generated by Django 3.2.5 on 2021-10-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0005_computer_request_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_request',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
