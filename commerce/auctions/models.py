from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class CommentModel(models.Model):
    comment_on_auction = models.TextField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.id}: {self.comment_on_auction}"

    
class BidModel(models.Model):
    bid_made = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.bid_made}"



class AuctionListingModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    initial_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bid = models.ForeignKey(BidModel, null=True,on_delete=models.SET_NULL, related_name="BidModel")
    sold = models.BooleanField(default=False)
    auction_image = models.URLField(max_length=200)
    category = models.CharField(max_length=30)
    # default_comment_id = 1 
    comments = models.ForeignKey(CommentModel,null=True, on_delete=models.SET_NULL, related_name="comments")

    def __str__(self):
        return f"{self.id}: {self.title}"




    

