# Generated by Django 2.0.2 on 2018-04-19 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displaybooks', '0004_auto_20180330_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='enable_comments',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discussion',
            name='datecreated',
            field=models.DateField(default=datetime.datetime(2018, 4, 19, 12, 18, 18, 271505)),
        ),
    ]
