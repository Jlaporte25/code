from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.username}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)
    category = models.CharField(max_length=64, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    is_active = models.BooleanField(default=True)
    
    def get_winner(self):
        return Winner.objects.filter(listing=self).first()
    
    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.amount}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    def __str__(self):
        return f"{self.comment}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist_user')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='watchlist_listing')
    def __str__(self):
        return f"{self.user} {self.listing}"

class Category(models.Model):
    name = models.CharField(max_length=64)
    listings = models.ManyToManyField(Listing, through='ListingCategory', related_name='categories')
    def __str__(self):
        return f"{self.name}"

class ListingCategory(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listing_category')
    def __str__(self):
        return f"{self.listing} {self.category}"

class Winner(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='winner')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.listing} {self.user} {self.amount}"

