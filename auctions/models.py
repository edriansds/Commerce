from email.policy import default
from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models
from sqlalchemy import ForeignKey

class User(AbstractUser):
    pass


class AuctionListings(models.Model):
    CATEGORIES = (
        ("Eletronic", "Eletronic"),
        ("Toys", "Toys"),
        ("Fashion", "Fashion"),
        ("Home", "Home"),
        ("Food", "Food"),
        ("Variety", "Variety")
    )
    title = models.CharField(max_length=48)
    description = models.TextField()
    category = models.CharField(max_length=24, null=True, blank=True, choices=CATEGORIES)
    image = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ManyToManyField(AuctionListings)

class Bids(models.Model):
    bid = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
    text = models.TextField(default="")
    timedate = models.DateTimeField(auto_now=True)

