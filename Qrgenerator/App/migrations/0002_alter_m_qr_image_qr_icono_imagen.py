# Generated by Django 5.1.3 on 2024-11-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_qr_image',
            name='qr_icono_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='qr_icon/'),
        ),
    ]
