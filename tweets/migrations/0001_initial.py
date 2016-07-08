# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_text', models.CharField(max_length=200)),
                ('tweet_location', models.CharField(max_length=200)),
                ('tweet_date', models.DateTimeField(verbose_name=b'date tweeted')),
                ('phrase', models.ForeignKey(to='tweets.Phrase')),
            ],
        ),
    ]
