# Generated by Django 4.2.16 on 2024-10-15 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='호텔명')),
                ('address', models.CharField(max_length=500, verbose_name='주소')),
                ('contact_number', models.CharField(max_length=20, verbose_name='연락처')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('description', models.TextField(blank=True, null=True, verbose_name='설명')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('reserved_by', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.meetingroom')),
            ],
            options={
                'verbose_name': '예약 관리',
                'verbose_name_plural': '예약 관리',
            },
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
