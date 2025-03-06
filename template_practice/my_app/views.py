from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {
        "name": "Winnie",
        "age": 56,
    }
    return render(request, "my_app/welcome.html", context)