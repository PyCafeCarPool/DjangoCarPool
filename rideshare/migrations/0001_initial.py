# Generated by Django 2.2.7 on 2019-11-24 23:16

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('driving_license', models.CharField(blank=True, default='', max_length=15)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(blank=True, default='', max_length=254)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideshare.Driver')),
            ],
        ),
    ]