# Generated by Django 3.1.2 on 2020-12-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20201208_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='revenue',
            field=models.FloatField(blank=True, max_length=200),
        ),
    ]
