# Generated by Django 3.2 on 2021-10-26 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211027_0100'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mail',
            new_name='OfficeMail',
        ),
    ]
