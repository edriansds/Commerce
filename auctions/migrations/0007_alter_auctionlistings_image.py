# Generated by Django 4.1.1 on 2022-10-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_initial_bid_auctionlistings_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
