# Generated by Django 3.1.6 on 2021-04-28 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0009_item_text2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text2',
            new_name='textID',
        ),
    ]
