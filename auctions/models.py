from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class AuctionListings(models.Model):
    CATEGORIES = (
        ("1", "Eletronic"),
        ("2", "Toys"),
        ("3", "Fashion"),
        ("4", "Home"),
        ("5", "Food")
    )
    title = models.CharField(max_length=48)
    description = models.TextField()
    initial_bid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=24, null=True, blank=True, choices=CATEGORIES)
    image = models.ImageField(null=True, blank=True)

class Bids(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
    auction_listings = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_listings = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
    text = models.TextField(default="")
    timedate = models.DateTimeField(auto_now=True)
