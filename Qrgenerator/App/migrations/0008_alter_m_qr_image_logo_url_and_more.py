# Generated by Django 5.1.3 on 2024-11-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_m_qr_image_logo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_qr_image',
            name='logo_url',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='m_qr_image',
            name='qr_icono_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]