# Generated by Django 3.1.3 on 2022-03-15 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bearID', models.IntegerField()),
                ('pTT_ID', models.IntegerField()),
                ('capture_lat', models.FloatField()),
                ('capture_long', models.FloatField()),
                ('sex', models.TextField()),
                ('age_class', models.TextField()),
                ('ear_applied', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploy_id', models.TextField()),
                ('recieved', models.TextField()),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
