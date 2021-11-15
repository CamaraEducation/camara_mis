# Generated by Django 3.2.5 on 2021-11-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211112_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='working_status',
            field=models.CharField(choices=[('Working', 'Working'), ('Problematic', 'Problematic'), ('Dispatched', 'Dispatched'), ('Processed', 'Processed'), ('E-Waste', 'E-Waste')], default='Processed', max_length=30),
        ),
    ]
