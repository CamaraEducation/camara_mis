# Generated by Django 3.2.5 on 2022-03-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0013_alter_computer_request_storage_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_request',
            name='memory_type',
            field=models.CharField(blank=True, choices=[('DRAM', 'DRAM'), ('SRAM', 'SRAM'), ('XEON', 'XEON')], default=None, max_length=30, null=True),
        ),
    ]
