# Generated by Django 2.2.12 on 2020-04-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_auto_20200429_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
