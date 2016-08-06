# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def load_fixture(apps, schema_editor):
    call_command('loaddata', '../fixtures/phrases.json')

class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
