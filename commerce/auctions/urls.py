from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>", views.product, name="product_index"),
    path("new/", views.create_new_listing, name="new"),
    path("watchlist/", views.WatchlistView, name="watchlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
