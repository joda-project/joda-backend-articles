# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-07 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('joda_core', '0004_i18n'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joda_core.Document')),
                ('pages', models.CharField(blank=True, max_length=32, verbose_name='pages')),
                ('volume', models.PositiveIntegerField(blank=True, null=True, verbose_name='volume')),
                ('issue', models.PositiveIntegerField(blank=True, null=True, verbose_name='issue')),
                ('year', models.PositiveIntegerField(blank=True, null=True, verbose_name='year')),
                ('doi', models.CharField(blank=True, max_length=255, verbose_name='DOI')),
                ('arxiv', models.CharField(blank=True, max_length=255, verbose_name='arXiv')),
                ('cds', models.CharField(blank=True, max_length=255, verbose_name='CDS')),
                ('authors', models.ManyToManyField(blank=True, to='joda_core.Author', verbose_name='authors')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
            bases=('joda_core.document',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='title')),
                ('abbr', models.CharField(blank=True, max_length=255, verbose_name='abbreviation')),
            ],
            options={
                'verbose_name': 'journal',
                'verbose_name_plural': 'journals',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='joda_articles.Journal', verbose_name='journal'),
        ),
    ]