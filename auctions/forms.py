from dataclasses import fields
from django import forms
from auctions.models import AuctionListings

class CreateListings(forms.ModelForm):
    class Meta:
        model = AuctionListings
        fields = ["title", "description", "bid",]
        