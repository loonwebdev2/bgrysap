# Generated by Django 3.1.6 on 2021-04-20 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0003_remove_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]