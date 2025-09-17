from django.forms import ModelForm
from django import forms
from .models import AuctionListingModel, BidModel, CommentModel
"""
class AuctionForm2(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=500)
    initial_price = forms.DecimalField(max_digits=6, decimal_places=2)
    # bid = forms.ModelChoiceField(queryset=BidModel.objects.all())
    # bid = forms.ForeignKey(BidModel, on_delete=models.CASCADE, related_name="BidModel")
    # sold = forms.BooleanField()
    auction_image = forms.URLField(max_length=200)
    category = forms.CharField(max_length=30)
    # comments = forms.ModelChoiceField(queryset=CommentModel.objects.all())
    # comments = forms.ForeignKey(CommentModel, blank=True, null=True,on_delete=models.SET_NULL, related_name="comments")
"""


class AuctionForm(ModelForm):
    class Meta:
        model = AuctionListingModel
        fields = ["title","description","initial_price", "auction_image", "category"]
