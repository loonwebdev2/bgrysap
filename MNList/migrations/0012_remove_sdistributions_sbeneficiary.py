# Generated by Django 3.1.6 on 2021-06-24 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0011_auto_20210624_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sdistributions',
            name='sbeneficiary',
        ),
    ]
