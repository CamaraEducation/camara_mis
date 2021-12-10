# Generated by Django 3.2.5 on 2021-12-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20211210_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='memory_type',
            field=models.CharField(choices=[('DRAM', 'DRAM'), ('SRAM', 'SRAM')], default='DRAM', max_length=10),
        ),
        migrations.AlterField(
            model_name='computer',
            name='os_version',
            field=models.CharField(blank=True, default='Linux', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='storage_type',
            field=models.CharField(choices=[('SDD', 'SSD'), ('HDD', 'HDD'), ('ROM', 'ROM'), ('SD Card', 'SD Card')], default='HDD', max_length=10),
        ),
    ]
