# Generated by Django 3.1.6 on 2021-04-25 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0006_auto_20210425_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='MNList.list'),
        ),
    ]