# Generated by Django 4.1.1 on 2022-10-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlistings',
            name='bids',
        ),
        migrations.RemoveField(
            model_name='auctionlistings',
            name='user',
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'Tech'), ('2', 'Toys'), ('3', 'Food'), ('4', 'Clothes'), ('5', 'House')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
