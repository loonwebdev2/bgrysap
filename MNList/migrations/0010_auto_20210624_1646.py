# Generated by Django 3.1.6 on 2021-06-24 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0009_auto_20210624_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slocation',
            old_name='dplace',
            new_name='dtype',
        ),
    ]