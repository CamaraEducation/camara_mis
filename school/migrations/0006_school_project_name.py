# Generated by Django 3.2.5 on 2022-02-11 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210817_0646'),
        ('school', '0005_auto_20211130_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='project_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
