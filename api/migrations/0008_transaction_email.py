# Generated by Django 3.2 on 2021-10-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20211024_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='email',
            field=models.CharField(default='', max_length=40),
        ),
    ]