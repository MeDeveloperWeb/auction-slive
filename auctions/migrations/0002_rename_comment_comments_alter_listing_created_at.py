# Generated by Django 4.0.5 on 2022-06-30 10:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 10, 6, 35, 797510, tzinfo=utc), editable=False),
        ),
    ]
