# Generated by Django 3.2.15 on 2022-09-16 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_rename_emailaddress_account_emails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='emails',
            new_name='email',
        ),
    ]
