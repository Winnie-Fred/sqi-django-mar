from django.urls import path

from . import views

app_name = "quote"

urlpatterns = [
    path("quote-of-the-day/", views.random_quote, name="quote_of_the_day"),
    path('get-random-quote/', views.get_random_quote, name="get_random_quote"),
]