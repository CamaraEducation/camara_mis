# Generated by Django 3.2.5 on 2021-10-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='female_sn_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='school',
            name='female_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='school',
            name='female_teachers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='school',
            name='male_sn_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='school',
            name='male_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='school',
            name='male_teachers',
            field=models.IntegerField(default=0),
        ),
    ]
