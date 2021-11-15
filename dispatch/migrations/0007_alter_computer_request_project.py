# Generated by Django 3.2.5 on 2021-11-05 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210817_0646'),
        ('dispatch', '0006_alter_computer_request_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_request',
            name='project',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
