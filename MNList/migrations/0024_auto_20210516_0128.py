# Generated by Django 3.1.6 on 2021-05-16 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0023_auto_20210516_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='ibrgy',
            name='bbrgy',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ibrgy',
            name='bbrgyID',
            field=models.TextField(default=''),
        ),
    ]