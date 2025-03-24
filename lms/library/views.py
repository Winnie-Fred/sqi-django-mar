from django.shortcuts import render, redirect

from authors.models import Author
from .models import Book
from .forms import BookForm, BookManualForm

# Create your views here.
def all_authors(request):
    return render(request, "library/all-authors.html")


def book_signings(request):
    return render(request, "library/book-signings.html")


def all_books(request):
    all_books = Book.objects.all()
    return render(request, "library/all-books.html", {"books": all_books})


def add_book_no_django_form(request):
    all_authors = Author.objects.all()

    context = {
        "authors": all_authors
    }
    if request.method == "POST":
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        no_of_pages = request.POST.get('number_of_pages')
        published_on = request.POST.get('published_on')
        cover_image = request.FILES.get('cover_image')

        author = Author.objects.get(id=author_id)
        print(author_id)

        Book.objects.create(title=title, author=author, number_of_pages=no_of_pages, published_on=published_on, cover_image=cover_image)
        return redirect('library:all_books')

    return render(request, "library/manual-form-create-book.html", context)


def add_book_with_django_form(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:all_books')

    context = {
        "form": form
    }
    return render(request, "library/auto-form-create-book copy.html", context)


def add_book_with_django_form_manual_render(request):
    form = BookForm()
    all_authors = Author.objects.all()


    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:all_books')

    context = {
        "form": form,
        "authors": all_authors,
    }
    return render(request, "library/manual-form-plus-django-form.html", context)


def add_book_with_django_forms_dot_form(request):
    form = BookManualForm()

    if request.method == "POST":
        form = BookManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get('title')
            author = cleaned_data.get('author')
            number_of_pages = cleaned_data.get('number_of_pages')
            published_on = cleaned_data.get('published_on')
            cover_image = cleaned_data.get('cover_image')
            Book.objects.create(title=title, author=author, number_of_pages=number_of_pages, published_on=published_on, cover_image=cover_image)
            return redirect('library:all_books')

    context = {
        "form": form
    }
    return render(request, "library/add-book-with-django-forms-dot-form.html", context)