# Generated by Django 3.2.5 on 2021-11-12 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210817_0646'),
        ('products', '0005_auto_20211111_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='device_status',
            field=models.CharField(choices=[('New', 'New'), ('Refurbished', 'Refurbished'), ('Used', 'Used')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='donor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.donor'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.supplier'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='working_status',
            field=models.CharField(choices=[('Working', 'Working'), ('Problematic', 'Problematic'), ('Dispatched', 'Dispatched'), ('Processed', 'Processed'), ('E-Waste', 'E-Waste')], default='Working', max_length=30),
        ),
    ]
