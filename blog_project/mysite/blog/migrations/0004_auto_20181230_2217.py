# Generated by Django 2.1.4 on 2018-12-30 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181230_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 16, 47, 6, 679559, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 16, 47, 6, 679165, tzinfo=utc)),
        ),
    ]
