# Generated by Django 3.1.1 on 2020-09-26 11:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loginfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=283)),
                ('department', models.CharField(choices=[('SD', 'Software Development'), ('STV', 'Software Testing'), ('HR', 'Human Resources'), ('DS', 'Data Science')], default='SD', max_length=4)),
                ('staff_id', models.IntegerField()),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 9, 26, 11, 5, 51, 722136, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='VisitorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=283)),
                ('visitor_name', models.CharField(max_length=283)),
                ('visitor_department', models.CharField(choices=[('SD', 'Software Development'), ('STV', 'Software Testing'), ('HR', 'Human Resources'), ('DS', 'Data Science')], default='SD', max_length=4)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 9, 26, 11, 5, 51, 722136, tzinfo=utc))),
            ],
        ),
    ]
