from django.shortcuts import render, HttpResponse

from .models import Order

# Create your views here.
# def orders(request):
    # if first_order is not None:
    #     print(first_order.total_price)
    # return HttpResponse("Coffee shop")

def some_view(request):
    first_order = Order.objects.last()
    print(first_order.total_price)
    return HttpResponse(f"Some View, {first_order.customer}")