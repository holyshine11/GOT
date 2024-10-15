# Generated by Django 4.2.16 on 2024-10-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='detail_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='상세 주소'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='postal_code',
            field=models.CharField(default='우편번호', max_length=5, verbose_name='우편번호'),
        ),
    ]
