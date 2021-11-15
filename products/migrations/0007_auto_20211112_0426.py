# Generated by Django 3.2.5 on 2021-11-12 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211112_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='screen_size',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('17 inch', '17 inch'), ('19 inch', '19 inch'), ('21 inch', '21 inch')], default='17 inch', max_length=20),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='screen_size',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('17 inch', '17 inch'), ('19 inch', '19 inch'), ('21 inch', '21 inch')], default='17 inch', max_length=20),
        ),
    ]
