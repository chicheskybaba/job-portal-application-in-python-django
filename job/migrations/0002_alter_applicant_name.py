# Generated by Django 4.1.3 on 2022-11-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
