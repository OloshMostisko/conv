# Generated by Django 3.2.8 on 2021-10-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_student_isregdone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='tranId',
            field=models.CharField(blank=True, default='', max_length=100, unique=True, verbose_name='Transction ID'),
        ),
    ]
