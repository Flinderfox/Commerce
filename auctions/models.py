from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return "(" + self.username + ", " + self.email + ")"
    #pass

# Create my models here.

class Product(models.Model):
    CATEGORIES = (
        ('FAS', 'Fashion'),
        ('TOY', 'Toys'),
        ('ELE', 'Electronics'),
        ('HOM', 'Home'),
        ('BEA', 'Beauty'),
        ('AUT', 'Automobiles')
    )
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length = 500)
    quantity = models.IntegerField()
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES
    )
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()

class Chat(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField()