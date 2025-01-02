from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Listing, User, Bid, Comment, Watchlist, Category, ListingCategory, Winner
from django.db.models import Max, Count
from django import forms

class NewAuctionForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    starting_bid = forms.DecimalField(label="Starting Bid")
    image = forms.URLField(label="Image URL", required=False)
    category = forms.CharField(label="Category")

class NewCommentForm(forms.Form):
    comment = forms.CharField(label="New Comment")

class NewBidForm(forms.Form):
    bid = forms.DecimalField(label="New Bid", max_digits=10, decimal_places=2)

def index(request):
    listings = Listing.objects.all()
    for listing in listings:
        winner = listing.get_winner()
        if winner:
            listing.winner_user = winner.user.username
        else:
            listing.winner_user = None
    return render(request, "auctions/index.html", {
        "listings": listings,
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
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


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
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")


def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing_comments = Comment.objects.filter(listing=listing)
    listing_bids = Bid.objects.filter(listing=listing)
    highest_bid = listing_bids.aggregate(Max('amount'))['amount__max']
    bid_count = listing_bids.aggregate(Count('id'))['id__count']
    in_watchlist = Watchlist.objects.filter(user=request.user, listing=listing).exists()
    is_owner = request.user == listing.created_by
    winner = listing.get_winner()
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "listing_comments": listing_comments,
        "highest_bid": highest_bid,
        "bid_count": bid_count,
        "comment_form": NewCommentForm(),
        "bid_form": NewBidForm(),
        "in_watchlist": in_watchlist,
        "is_owner": is_owner,
        "is_active": listing.is_active,
        "winner": winner,
    })


def create(request):
    if request.method == "POST":
        form = NewAuctionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            image = form.cleaned_data["image"]
            category_name = form.cleaned_data["category"]
            created_by = User.objects.get(pk=request.user.id)
            listing = Listing.objects.create(title=title, description=description, starting_bid=starting_bid, image=image, category=category_name, created_by=created_by, is_active=True)
            listing.save()
            
            category, created = Category.objects.get_or_create(name=category_name)
            category.listings.add(listing)
            return redirect("auctions:index")
        else:
            return render(request, "auctions/create.html", {
                "form": form
            })
    else:
        return render(request, "auctions/create.html", {
            "form": NewAuctionForm()
        })


def watchlist(request):
    watchlists = Watchlist.objects.filter(user=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlists": watchlists
    })


def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories,
    })


def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    listings = category.listings.all()
    return render(request, "auctions/category.html", {
        "listings": listings,
        "category": category,
    })


def close(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.user == listing.created_by:
        listing.is_active = False
        listing.save()
        winner_bid = Bid.objects.filter(listing=listing).order_by('-amount').first()
        if winner_bid:
            listing.winner_set.create(user=winner_bid.user, amount=winner_bid.amount)
        return redirect(reverse('auctions:listing', args=[listing_id]))
    else:
        return redirect(reverse('auctions:index', args=[listing_id]))


def comment(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data["comment"]
            created_by = User.objects.get(pk=request.user.id)
            Comment.objects.create(comment=comment_text, created_by=created_by, listing=listing)
    return redirect(reverse('auctions:listing', args=[listing_id]))


def bid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if not listing.is_active:
        return redirect(reverse('auctions:listing', args=[listing_id]))
    
    if request.method == "POST":
        form = NewBidForm(request.POST)
        if form.is_valid():
            bid_amount = form.cleaned_data["bid"]
            created_by = User.objects.get(pk=request.user.id)
            Bid.objects.create(amount=bid_amount, user=created_by, listing=listing)
    return redirect(reverse('auctions:listing', args=[listing_id]))


def add_watchlist(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        created_by = User.objects.get(pk=request.user.id)
        Watchlist.objects.create(user=created_by, listing=listing)
    return redirect(reverse('auctions:listing', args=[listing_id]))


def remove_watchlist(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        created_by = User.objects.get(pk=request.user.id)
        Watchlist.objects.filter(user=created_by, listing=listing).delete()
    return redirect(reverse('auctions:listing', args=[listing_id]))