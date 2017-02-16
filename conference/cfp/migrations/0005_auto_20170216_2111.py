# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0004_auto_20161210_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='proposal_audience',
            field=models.CharField(verbose_name='Audience', choices=[('every', 'Everyone'), ('beginner', 'Beginner'), ('inter', 'Intermediate'), ('advanced', 'Advanced')], max_length=10),
        ),
        migrations.AlterField(
            model_name='workshopsubmission',
            name='proposal_audience',
            field=models.CharField(verbose_name='Audience', choices=[('every', 'Everyone'), ('beginner', 'Beginner'), ('inter', 'Intermediate'), ('advanced', 'Advanced')], max_length=10),
        ),
    ]
