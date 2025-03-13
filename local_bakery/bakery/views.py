from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "bakery/home.html")

def about(request):
    return render(request, "bakery/about.html")

def menu(request):
    bakery_menu = {
        "Croissant": 2.50,
        "Chocolate Chip Cookie": 1.75,
        "Blueberry Muffin": 3.00,
        "Cinnamon Roll": 3.50,
        "Baguette": 4.00,
        "Cheesecake Slice": 5.50,
        "Apple Pie Slice": 4.75,
        "Cupcake": 3.25
    }
    context = {
        'menu':bakery_menu
    }
    return render(request, "bakery/menu.html", context)

def contact(request):
    return render(request, "bakery/contact.html")