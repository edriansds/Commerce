from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from sqlalchemy import ForeignKey

class User(AbstractUser):
    pass


class AuctionListings(models.Model):
    CATEGORIES = (
        ("Tech", "Eletronic"),
        ("Toys", "Toys"),
        ("Fashion", "Fashion"),
        ("Home", "Home"),
        ("Food", "Food")
    )
    title = models.CharField(max_length=48)
    description = models.TextField()
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=24, null=True, blank=True, choices=CATEGORIES)
    image = models.URLField(null=True, blank=True)

class Bids(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
    auction_listings = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_listings = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
    text = models.TextField(default="")
    timedate = models.DateTimeField(auto_now=True)

