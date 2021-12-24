# Generated by Django 3.2.5 on 2021-12-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20211214_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='working_status',
            field=models.CharField(choices=[('Working', 'Working'), ('Processed', 'Processed'), ('Problematic', 'Problematic'), ('Dispatched', 'Dispatched'), ('E-Waste', 'E-Waste'), ('Not Received', 'Not Received')], default='Working', max_length=30),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='working_status',
            field=models.CharField(choices=[('Processed', 'Processed'), ('Problematic', 'Problematic'), ('Dispatched', 'Dispatched'), ('E-Waste', 'E-Waste'), ('Not Received', 'Not Received')], default='Processed', max_length=30),
        ),
    ]