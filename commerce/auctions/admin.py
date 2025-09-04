from django.contrib import admin
from .models import BidModel, AuctionListingModel, CommentModel

# Register your models here.
admin.site.register(AuctionListingModel)
admin.site.register(BidModel)
admin.site.register(CommentModel)