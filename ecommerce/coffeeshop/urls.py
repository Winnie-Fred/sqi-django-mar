from django.urls import path

from . import views

app_name = "coffeeshop"

urlpatterns = [
    # path('orders/', views.orders, name="orders"),   
    path('some-view/', views.some_view, name="some_view"),   
]