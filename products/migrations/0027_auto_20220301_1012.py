# Generated by Django 3.2.5 on 2022-03-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20220227_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.CharField(choices=[('Dell', 'Dell'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Epson', 'Epson'), ('MediTech', 'MediTech'), ('Samsung', 'Samsung'), ('X_Tig', 'X_Tig'), ('Fujitsu', 'Fujitsu'), ('Clone', 'Clone'), ('P.C Peripherals', 'P.C Peripherals'), ('Stone PC', 'Stone PC'), ('System manufacturer', 'System manufacturer')], max_length=20),
        ),
        migrations.AlterField(
            model_name='computer',
            name='storage_size',
            field=models.CharField(choices=[('80 GB', '80 GB'), ('128 GB', '128 GB'), ('160 GB', '160 GB'), ('250 GB', '250 GB'), ('320 GB', '320 GB'), ('500 GB', '500 GB'), ('1 TB', '1 TB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB')], max_length=10),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='brand',
            field=models.CharField(choices=[('Dell', 'Dell'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Epson', 'Epson'), ('MediTech', 'MediTech'), ('Samsung', 'Samsung'), ('X_Tig', 'X_Tig'), ('Fujitsu', 'Fujitsu'), ('Clone', 'Clone'), ('P.C Peripherals', 'P.C Peripherals'), ('Stone PC', 'Stone PC'), ('System manufacturer', 'System manufacturer')], max_length=20),
        ),
    ]
