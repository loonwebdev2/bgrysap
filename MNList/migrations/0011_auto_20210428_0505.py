# Generated by Django 3.1.6 on 2021-04-28 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0010_auto_20210428_0429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
        migrations.RemoveField(
            model_name='item',
            name='textID',
        ),
        migrations.AddField(
            model_name='list',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='list',
            name='textID',
            field=models.TextField(default=''),
        ),
    ]
