# Generated by Django 3.1.6 on 2021-04-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0017_auto_20210429_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='text',
        ),
        migrations.RemoveField(
            model_name='info',
            name='textID',
        ),
        migrations.AddField(
            model_name='ibrgy',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ibrgy',
            name='textID',
            field=models.TextField(default=''),
        ),
    ]