# Generated by Django 3.2.5 on 2022-02-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_computer_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='serial_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
