# Generated by Django 3.2.15 on 2022-09-17 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_rename_emails_account_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='gender',
        ),
    ]
