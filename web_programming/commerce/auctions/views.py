from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Listing, User, Bid, Comment, Watchlist, Category, ListingCategory, Winner
from django import forms

class NewAuctionForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    starting_bid = forms.DecimalField(label="Starting Bid")
    image = forms.URLField(label="Image URL")
    category = forms.CharField(label="Category")

def index(request):
    if request.user.is_authenticated:
        return render(request, "auctions/index.html", {
            "listings": Listing.objects.all(),
            "watchlist": User.objects.get(pk=request.user.id).watchlist.all()
        })
    else:
        return render(request, "auctions/index.html", {
            "listings": Listing.objects.all()
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
    else:
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


def listing(request):
    
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk=id),
        
    })


def create(request):
    if request.method == "POST":
        form = NewAuctionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            image = form.cleaned_data["image"]
            category = form.cleaned_data["category"]
            created_by = User.objects.get(pk=request.user.id)
            listing = Listing.objects.create(title=title, description=description, starting_bid=starting_bid, image=image, category=category, created_by=created_by)
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", {
                "form": form
            })
    else:
        return render(request, "auctions/create.html", {
            "form": NewAuctionForm()
        })


def watchlist(request):
    return render(request, "auctions/watchlist.html")


def categories(request):
    return render(request, "auctions/categories.html")


def category(request):
    return render(request, "auctions/category.html")


def close(request):
    return render(request, "auctions/close.html")


def comment(request):
    return render(request, "auctions/comment.html")


def bid(request):
    return render(request, "auctions/bid.html")


def add_watchlist(request):
    return render(request, "auctions/add_watchlist.html")


def remove_watchlist(request):
    return render(request, "auctions/remove_watchlist.html")
