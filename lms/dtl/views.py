from django.shortcuts import render

from django.utils import timezone

# Create your views here.
def dtl_syntax(request):
    context = {
        "name": "Winifred",
        "age": 35,
        "is_happy": False,
        "numbers": [],
        "data": {"state": "Oyo", "gender": "Female"}
    }
    return render(request, "dtl/syntax.html", context)


def cart(request):
    cart_items = ["tomato", "strawberry", "burger", "cake"]
    context = {
        "user": "winifred igboama",
        "cart_items": cart_items,
        "is_favorite": True,
        "no_of_items_in_cart": len(cart_items),
        "today": timezone.now(),
    }
    return render(request, "dtl/cart.html", context)