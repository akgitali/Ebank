# Generated by Django 3.2.15 on 2022-09-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='contectno',
            field=models.CharField(max_length=12),
        ),
    ]
