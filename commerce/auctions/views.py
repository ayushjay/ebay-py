from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, BidModel, AuctionListingModel, CommentModel
from .forms import AuctionForm

def index(request):
    
    return render(request, "auctions/index.html",{
        "context": AuctionListingModel.objects.all(),
    })

def product(request, product_id):
    product = AuctionListingModel.objects.get(id=product_id)
    return render(request, "auctions/product_listing.html", {
        "product":product,
    })

@login_required(login_url="/login")
def create_new_listing(request):
        
        if request.method == "POST":
            form = AuctionForm(request.POST)
            if form.is_valid():
                # title = form.cleaned_data["title"]
                # description= form.cleaned_data["description"]
                # initial_price = form.cleaned_data["initial_price"]
                # auction_image= form.cleaned_data["auction_image"]
                # category= form.cleaned_data["category"]

                # # MOST IMP LINE I MISSED
                      
                # AuctionListingModel.objects.create(title=title,  description= description, initial_price= initial_price, auction_image=auction_image,category=category)
                form.save()
                return render(request, "auctions/index.html",{
                    "context": AuctionListingModel.objects.all(),          
        })
        else:
            # return render(request, "auctions/add_auction_listing.html", {
            #     "form":form,
            #     })
            form = AuctionForm()
        return render(request, "auctions/add_auction_listing.html", {
                "form":form,
                })

""" @login_required(login_url="/login")
def product_listing_view(request,product_id):
    product = AuctionListingModel.objects.get(id=product_id)
    return render(request,"auctions/product_listing.html",{
         "product":product,}) """
       

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
