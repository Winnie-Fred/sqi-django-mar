from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('all-authors/', views.all_authors, name='authors'),
    path('all-books/', views.all_books, name='all_books'),
    path('book-signings/', views.book_signings, name='book_signings'),
    path('add-book-no-django-form/', views.add_book_no_django_form, name="add_book_no_django_form"),
    path('add-book-with-django-form/', views.add_book_with_django_form, name="add_book_with_django_form"),
    path('add-book-with-django-form-manual-render/', views.add_book_with_django_form_manual_render, name="add_book_with_django_form_manual_render"),
]