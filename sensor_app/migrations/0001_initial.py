# Generated by Django 3.0.5 on 2020-04-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sensorId', models.AutoField(primary_key=True, serialize=False)),
                ('sensorType', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
