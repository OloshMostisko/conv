# Generated by Django 3.2.8 on 2021-10-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_officemail_officeemail4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officemail',
            name='accounceOfficeEmail',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Accounce Email'),
        ),
        migrations.AlterField(
            model_name='officemail',
            name='officeEmail1',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Other office email 1'),
        ),
        migrations.AlterField(
            model_name='officemail',
            name='officeEmail2',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Other office email 2'),
        ),
        migrations.AlterField(
            model_name='officemail',
            name='officeEmail3',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Other office email 3'),
        ),
        migrations.AlterField(
            model_name='officemail',
            name='officeEmail4',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Other office email 4'),
        ),
        migrations.AlterField(
            model_name='officemail',
            name='regOfficeEmail',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Reg Office Email'),
        ),
    ]
