# Generated by Django 3.2.5 on 2021-12-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20211210_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.CharField(choices=[('Dell', 'Dell'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Epson', 'Epson'), ('MediTech', 'MediTech'), ('Samsung', 'Samsung'), ('X_Tig', 'X_Tig')], max_length=20),
        ),
        migrations.AlterField(
            model_name='computer',
            name='device_status',
            field=models.CharField(choices=[('Refurbished', 'Refurbished'), ('New', 'New'), ('Used', 'Used')], default='Refurbished', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='os_type',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Mac OS', 'Mac OS'), ('Windows', 'Windows'), ('Android', 'Android'), ('No OS', 'No OS')], default='Linux', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='processor_type',
            field=models.CharField(choices=[('intel i3', 'intel i3'), ('intel i5', 'intel i5'), ('intel i7', 'intel i7'), ('Dual Core', 'Dual Core'), ('Pentium 4', 'Pentium 4'), ('Quad Core', 'Quad Core'), ('AMD', 'AMD')], max_length=20),
        ),
        migrations.AlterField(
            model_name='computer',
            name='screen_size',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('15 INCH', '15 inch'), ('17 inch', '17 inch'), ('19 inch', '19 inch'), ('20 INCH', '20 inch'), ('21 inch', '21 inch')], default='17 inch', max_length=20),
        ),
        migrations.AlterField(
            model_name='computer',
            name='storage_size',
            field=models.CharField(choices=[('80 GB', '80 GB'), ('128 GB', '128 GB'), ('160 GB', '160 GB'), ('250 GB', '250 GB'), ('320 GB', '320 GB'), ('500 GB', '500 GB'), ('1TB', '1TB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB')], max_length=10),
        ),
        migrations.AlterField(
            model_name='computer',
            name='storage_type',
            field=models.CharField(choices=[('HDD', 'HDD'), ('SDD', 'SSD'), ('ROM', 'ROM'), ('SD Card', 'SD Card')], default='HDD', max_length=10),
        ),
        migrations.AlterField(
            model_name='computer',
            name='working_status',
            field=models.CharField(choices=[('Working', 'Working'), ('Processed', 'Processed'), ('Problematic', 'Problematic'), ('Dispatched', 'Dispatched'), ('E-Waste', 'E-Waste')], default='Working', max_length=30),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='brand',
            field=models.CharField(choices=[('Dell', 'Dell'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Epson', 'Epson'), ('MediTech', 'MediTech'), ('Samsung', 'Samsung'), ('X_Tig', 'X_Tig')], max_length=20),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='device_status',
            field=models.CharField(choices=[('Refurbished', 'Refurbished'), ('New', 'New'), ('Used', 'Used')], default='Refurbished', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='screen_size',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('15 INCH', '15 inch'), ('17 inch', '17 inch'), ('19 inch', '19 inch'), ('20 INCH', '20 inch'), ('21 inch', '21 inch')], default='17 inch', max_length=20),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='working_status',
            field=models.CharField(choices=[('Processed', 'Processed'), ('Problematic', 'Problematic'), ('Dispatched', 'Dispatched'), ('E-Waste', 'E-Waste')], default='Processed', max_length=30),
        ),
    ]
