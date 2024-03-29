# Generated by Django 3.2.5 on 2022-02-14 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_monitor_working_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
