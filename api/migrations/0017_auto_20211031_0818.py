# Generated by Django 3.1.7 on 2021-10-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_registration_totaldegree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='secondDegree_id',
        ),
        migrations.AlterField(
            model_name='registration',
            name='photo',
            field=models.FileField(default='Student_Documents/black-solid.jpg', null=True, upload_to='Student_Documents/'),
        ),
    ]
