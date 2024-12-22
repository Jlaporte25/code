from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
    watchlist = models.ManyToManyField('Listing', blank=True, related_name='watchlist')
    def __str__(self):
        return f"{self.username}"
    
class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)
    category = models.CharField(max_length=64, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    is_active = models.BooleanField(default=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
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
    def __str__(self):
        return f"{self.listing} {self.user}"

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    image = models.URLField()
    def __str__(self):
        return f"{self.image}"

class ListingBid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_bids')
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='listing_bids')
    def __str__(self):
        return f"{self.listing} {self.bid}"

class ListingComment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_comments')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='listing_comments')
    def __str__(self):
        return f"{self.listing} {self.comment}"

