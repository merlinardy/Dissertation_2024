# Generated by Django 4.2.6 on 2023-11-01 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='accessible',
            field=models.BooleanField(default=True),
        ),
    ]
