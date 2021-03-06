# Generated by Django 3.0.1 on 2020-01-02 01:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', models.TextField(verbose_name='Description')),
                ('author', models.CharField(max_length=128, verbose_name='author')),
                ('pub_date', models.DateTimeField(verbose_name='Publish Date')),
                ('guid', models.CharField(max_length=40, verbose_name='GUID')),
                ('guid_verbatim', models.CharField(max_length=100, verbose_name='GUID')),
                ('dwc_core_type', models.CharField(max_length=128, verbose_name='Dw-C Core Type')),
                ('data_license', models.CharField(max_length=128, verbose_name='Data License')),
                ('stats_num_record', models.PositiveIntegerField(default=0)),
                ('stats_num_occurrence', models.PositiveIntegerField(default=0)),
                ('stats_extensions', django.contrib.postgres.fields.jsonb.JSONField()),
                ('is_most_project', models.BooleanField(default=False, verbose_name='是否為科技部計畫')),
            ],
        ),
        migrations.CreateModel(
            name='TaxonTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('rank_map', models.CharField(max_length=256, verbose_name='rank map')),
            ],
        ),
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=32, verbose_name='rank')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('name_zh', models.CharField(max_length=128, verbose_name='name_zh')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='count')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Taxon')),
                ('tree', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.TaxonTree')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
