from django.shortcuts import render

from review.models import Author

# Create your views here.
def home(request):
    return render(request, "pages/index.html")


def authors(request):
    return render(request, "pages/authors.html", {"authors": Author.objects.all()})

