from unicodedata import category, decimal
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListings(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=28)
    description = models.TextField()
    bid = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.URLField()


class Bids(models.Model):
    pass


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commment = models.TextField()
    timedate = models.DateTimeField()
