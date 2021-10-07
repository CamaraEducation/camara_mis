# Generated by Django 3.2.5 on 2021-10-07 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0003_alter_school_email'),
        ('projects', '0009_auto_20210817_0646'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(help_text='Short code to identify the course (must be unique).', max_length=20, unique=True)),
                ('course_target', models.CharField(help_text='The target group of the course', max_length=100)),
                ('course_description', models.CharField(max_length=250)),
                ('course_certificate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10)),
                ('course_version', models.CharField(blank=True, default=None, max_length=20)),
                ('course_delivery', models.CharField(choices=[('Online', 'Online'), ('Face-to-Face', 'Face-to-Face')], max_length=20)),
                ('course_duration', models.IntegerField(help_text='Estimated course duration in hours.')),
                ('course_price', models.CharField(blank=True, default=None, max_length=20)),
                ('course_cost', models.CharField(blank=True, default=None, max_length=20)),
                ('course_status', models.CharField(choices=[('Not Active', 'Not Active'), ('Active', 'Active')], max_length=20)),
                ('course_designed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
                ('hub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hub')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=250)),
                ('number_of_participant', models.IntegerField()),
                ('number_of_schools', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('traing_duration', models.IntegerField(help_text='The training duration in hours.')),
                ('training_location', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('Started', 'Started'), ('Completed', 'Completed')], max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Training_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('subject_thought', models.CharField(max_length=30)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.training')),
            ],
        ),
    ]
