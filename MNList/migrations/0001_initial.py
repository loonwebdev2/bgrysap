# Generated by Django 3.1.6 on 2021-06-27 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BResidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rlname', models.TextField(default='')),
                ('rfname', models.TextField(default='')),
                ('rmname', models.TextField(default='')),
                ('rrelation', models.TextField(default='')),
                ('rjob', models.TextField(default='')),
                ('rnumber', models.IntegerField(default='')),
                ('radd', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='IBrgy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mncplty', models.TextField(default='')),
                ('bname', models.TextField(default='')),
                ('bID', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='SBeneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stranche', models.TextField(default='')),
                ('sincome', models.IntegerField(default='')),
                ('scategory', models.TextField(default='')),
                ('sclass', models.TextField(default='')),
                ('samount', models.TextField(default='')),
                ('bresidents', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MNList.bresidents')),
            ],
        ),
        migrations.CreateModel(
            name='SDistributions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dmode', models.TextField(default='')),
                ('dtype', models.TextField(default='')),
                ('dlocation', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Statusdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddate', models.DateField(default='')),
                ('dstatus', models.TextField(default='')),
                ('dperson', models.TextField(default='')),
                ('dremarks', models.TextField(default='')),
                ('bresidents', models.ManyToManyField(default=None, to='MNList.BResidents')),
                ('sbeneficiary', models.ManyToManyField(default=None, to='MNList.SBeneficiary')),
                ('sdistribution', models.ManyToManyField(default=None, to='MNList.SDistributions')),
            ],
        ),
        migrations.AddField(
            model_name='bresidents',
            name='ibrgy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MNList.ibrgy'),
        ),
    ]
