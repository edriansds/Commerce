from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import CreateListings, PlaceBid, WriteComments
from .models import User, AuctionListings, Bids, Comments, Watchlist


def index(request):
    listings = AuctionListings.objects.all().values()
    bid = Bids.objects.all().values()
    return render(request, "auctions/index.html", {
        "listings": listings,
        "bids": bid,
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
        listing_form = CreateListings(request.POST)
        bid_form = PlaceBid(request.POST)

        if listing_form.is_valid() and bid_form.is_valid():
            listing = listing_form.save(commit=False)
            listing.user = request.user
            listing.save()

            bid = bid_form.save(commit=False)
            bid.user = request.user
            bid.listing = AuctionListings(listing.id)
            bid.save()

            return HttpResponseRedirect(reverse("index"))
        else:

            # If any validation problem
            listing_form = CreateListings()
            bid_form = PlaceBid()

            return render(request, "auctions/create.html",{
                "message": "Fill all the required fields",
                "listing_form": listing_form,
                "bid_form": bid_form,
            })
    else:
        listing_form = CreateListings()
        bid_form = PlaceBid()

        return render(request, "auctions/create.html", {
            "listing_form": listing_form,
            "bid_form": bid_form,
        })


def listing(request, listing_id):
    if request.method == "POST":

        # Close a bid
        if "cb" in request.POST:
            AuctionListings.objects.filter(id=listing_id).update(active=False)

            return HttpResponseRedirect(reverse("listings", args=[listing_id]))

        # Add or remove from watchlist
        elif "wl" in request.POST:
            listing = AuctionListings.objects.get(id=listing_id)
            obj, created = Watchlist.objects.get_or_create(user=request.user)

            if listing in obj.listing.all():
                obj.listing.remove(listing)
            else:
                obj.listing.add(listing)    
            return HttpResponseRedirect(reverse("listings", args=[listing_id]))

        elif "text" in request.POST:

            # Validate Comments
            form = WriteComments(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.listing = AuctionListings(id=listing_id)
                comment.user = request.user
                comment.save()

                return HttpResponseRedirect(reverse("listings", args=[listing_id]))

        elif "bid" in request.POST:
            try:
                form = PlaceBid(request.POST)
                bid = float(request.POST["bid"])
            except ValueError: 
                return HttpResponse("OPS")

            if form.is_valid():
                all_bids = Bids.objects.filter(listing=listing_id).values("bid")

                for current_bid in all_bids:
                    if not bid > float(current_bid["bid"]):
                        return HttpResponseRedirect(reverse("listings", args=[listing_id]))
                
                actual_bid = form.save(commit=False)
                actual_bid.user = request.user
                actual_bid.listing = AuctionListings(id=listing_id)
                actual_bid.save()
            
            # Validate Price
            return HttpResponseRedirect(reverse("listings", args=[listing_id]))
    else:
        listing = AuctionListings.objects.get(id=listing_id)

        # Get all the bid information
        bids = Bids.objects.filter(listing=listing_id).values()
        bid = bids.order_by("-bid").first()
        bid_user = User.objects.filter(id=bid["user_id"]).values('username')
        bid["username"] = bid_user[0]['username']
        
        bid_form = PlaceBid()
        comment_form = WriteComments()
        comments = Comments.objects.filter(listing=listing_id)
        try:
            watchlist = Watchlist.objects.filter(user=request.user, listing=listing_id)
        except TypeError:
            watchlist = None

        context = {
            "listing": listing,
            "bid": bid,
            "bid_form": bid_form,
            "comments": comments,
            "comment_form": comment_form,
            "watchlist": watchlist,
        }
        return render(request, "auctions/listing.html", context)


@login_required
def watchlist(request):
    watchlist = Watchlist.objects.values()
    print(watchlist)

    context = {
        "watchlist": watchlist,
    }
    return render(request, "auctions/watchlist.html", context)