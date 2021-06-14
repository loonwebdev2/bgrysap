# Generated by Django 3.1.6 on 2021-06-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MNList', '0037_sdistributions_dplace'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusdb',
            name='sdistributions',
        ),
        migrations.AddField(
            model_name='statusdb',
            name='bresidents',
            field=models.ManyToManyField(default=None, to='MNList.BResidents'),
        ),
        migrations.AddField(
            model_name='statusdb',
            name='sbeneficiary',
            field=models.ManyToManyField(default=None, to='MNList.SBeneficiary'),
        ),
    ]
