# Generated by Django 3.1.7 on 2021-10-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20211030_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='intake',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='registration',
            name='p_username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
