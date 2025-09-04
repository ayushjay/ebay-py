from django.forms import ModelForm
from .models import AuctionListingModel, BidModel, CommentModel



class AuctionForm(ModelForm):
    class Meta:
        model = AuctionListingModel
        fields = ["title","description","initial_price", "auction_image", "category"]
