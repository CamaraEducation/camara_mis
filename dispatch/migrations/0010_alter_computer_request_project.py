# Generated by Django 3.2.5 on 2021-11-05 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210817_0646'),
        ('dispatch', '0009_auto_20211105_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer_request',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
