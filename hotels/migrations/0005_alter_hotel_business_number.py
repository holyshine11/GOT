# Generated by Django 4.2.16 on 2024-10-16 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_alter_hotel_business_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='business_number',
            field=models.CharField(default='', max_length=12, verbose_name='사업자 번호'),
        ),
    ]
