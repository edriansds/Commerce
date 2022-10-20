from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import CreateListings, PlaceBid, WriteComments
from .models import User, AuctionListings, Bids, Comments


def index(request):
    auctions_listings = AuctionListings.objects.all().values()
    return render(request, "auctions/index.html", {
        "auction_listings": auctions_listings,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create(request):
    if request.method == "POST":
        
        # Check if the form is valid
        form = CreateListings(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:

            # If any validation problem
            form = CreateListings()
            return render(request, "auctions/create.html",{
                "message": "Fill all the required fields",
                "form": form,
            })
    else:
        form = CreateListings()
    return render(request, "auctions/create.html", {
        "form": form,
    })


def listing(request, listing_id):
    if request.method == "POST":
        return HttpResponse("")
    else:
        listing = AuctionListings.objects.get(id=listing_id)
        form = PlaceBid()
        comment_form = WriteComments()
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "form": form,
            "comment_form": comment_form,
        })