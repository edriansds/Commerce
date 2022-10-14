from dataclasses import fields
from django import forms
from auctions.models import AuctionListings

class CreateListings(forms.ModelForm):
    class Meta:
        model = AuctionListings
        fields = ["title", "description", "bid", "category", "image"]
        labels = {
            "title": "Title",
            "description": "Description",
            "bid": "Initial Bid",
            "category": "Category",
            "image": "Image",
        }   
    def __init__(self, *args, **kwargs):
        super(CreateListings, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'
            field.field.widget.attrs['autocomplete'] = 'off'