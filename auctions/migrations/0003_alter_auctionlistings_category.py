# Generated by Django 4.1.1 on 2022-10-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_auctionlistings_bids_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'Eletronic'), ('2', 'Toys'), ('3', 'Fashion'), ('4', 'Home')], max_length=24, null=True),
        ),
    ]