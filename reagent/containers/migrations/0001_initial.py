# Generated by Django 5.0.2 on 2024-03-03 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('expiration_date', models.DateTimeField(default=datetime.datetime(2027, 2, 16, 8, 33, 17, 943282))),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'containers',
            },
        ),
    ]
