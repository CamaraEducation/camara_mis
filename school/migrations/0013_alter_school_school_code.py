# Generated by Django 3.2.5 on 2022-03-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_sub_county_zone_hub_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_code',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]