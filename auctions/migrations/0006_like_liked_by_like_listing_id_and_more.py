# Generated by Django 4.0.5 on 2022-06-30 12:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_listing_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='liked_by',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, related_name='lover', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='listing_id',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, related_name='listing_obj', to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 12, 41, 55, 776674, tzinfo=utc), editable=False),
        ),
    ]
