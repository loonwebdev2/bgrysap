# Generated by Django 3.1.6 on 2021-06-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0003_auto_20210627_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusdbs',
            name='ddate',
            field=models.DateField(default=''),
        ),
    ]
