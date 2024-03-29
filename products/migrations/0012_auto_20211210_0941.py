# Generated by Django 3.2.5 on 2021-12-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20211210_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='os_type',
            field=models.CharField(choices=[('Mac OS', 'Mac OS'), ('Windows', 'Windows'), ('Linux', 'Linux')], default='Linux', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='os_version',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
