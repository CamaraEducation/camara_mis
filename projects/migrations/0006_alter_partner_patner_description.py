# Generated by Django 3.2.5 on 2021-08-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210810_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='patner_description',
            field=models.TextField(blank=True, default=None, help_text='Short description of the partners expertise and how it fits with Camara'),
        ),
    ]
