from django.shortcuts import render, HttpResponse

# Create your views here.
def about_us(request):
    return HttpResponse("This is some info about us")


def contact(request):
    return HttpResponse("Call us on this number: 09030556541")