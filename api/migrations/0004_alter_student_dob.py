# Generated by Django 3.2 on 2021-10-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_student_tranid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateTimeField(verbose_name='Dath Of Birth'),
        ),
    ]
