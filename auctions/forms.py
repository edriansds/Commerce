from django import forms
from auctions.models import Listings, Bids, Comments

class CreateListings(forms.ModelForm):
    class Meta:
        model = Listings
        fields = ["title", "description", "category", "image"]
        labels = {
            "title": "Title",
            "description": "Description",
            "category": "Category",
            "image": "Image",
        }   
    def __init__(self, *args, **kwargs):
        super(CreateListings, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'
            field.field.widget.attrs['autocomplete'] = 'off'


class PlaceBid(forms.ModelForm):
    class Meta:
        model = Bids
        fields = ["bid"]
        labels = {
            "bid": 'Bid',
        }

    def __init__(self, *args, **kwargs):
        super(PlaceBid, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'
            field.field.widget.attrs['autocomplete'] = 'off'


class WriteComments(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]
        labels = {
            "text": ''
        }

    def __init__(self, *args, **kwargs):
        super(WriteComments, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'
            field.field.widget.attrs['autocomplete'] = 'off'
            field.field.widget.attrs['name'] = 'comment'
