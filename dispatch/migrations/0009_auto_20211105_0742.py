# Generated by Django 3.2.5 on 2021-11-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0008_alter_computer_request_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_request',
            name='computer_status',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Refurbished', 'Refurbished'), ('Used', 'Used')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='computer_type',
            field=models.CharField(blank=True, choices=[('System Unit', 'System Unit'), ('Tablet', 'Tablet'), ('Laptop', 'Laptop'), ('Printer', 'Printer'), ('Projector', 'Projector')], default=None, help_text='If its laptop, CPU, tablet etc', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='memory_size',
            field=models.CharField(blank=True, choices=[('512MB', '512MB'), ('1GB', '1GB'), ('2GB', '2GB'), ('4GB', '4GB'), ('8GB', '8GB')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='memory_type',
            field=models.CharField(blank=True, choices=[('DRAM', 'DRAM'), ('SRAM', 'SRAM')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='os_type',
            field=models.CharField(blank=True, choices=[('Mac OS', 'Mac OS'), ('Windows', 'Windows'), ('Linux', 'Linux')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='os_version',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='processor_speed',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='processor_type',
            field=models.CharField(blank=True, choices=[('intel i3', 'intel i3'), ('intel i5', 'intel i5'), ('intel i7', 'intel i7'), ('Dual Core', 'Dual Core')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='request_notes',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='storage_size',
            field=models.CharField(blank=True, choices=[('80GB', '80GB'), ('128GB', '128GB'), ('160GB', '160GB'), ('250GB', '250GB'), ('320GB', '320GB'), ('500GB', '500GB'), ('1TB', '1TB')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='computer_request',
            name='storage_type',
            field=models.CharField(blank=True, choices=[('SDD', 'SSD'), ('HDD', 'HDD'), ('ROM', 'ROM'), ('SD Card', 'SD Card')], default=None, max_length=30, null=True),
        ),
    ]
