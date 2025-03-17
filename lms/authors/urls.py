from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.home, name='home'),
    path('book-list/', views.book_list, name='book_list'),
    path('authors-and-books/', views.authors_and_books, name="authors_and_books"),
    path('author/<int:author_id>/', views.author, name="author_detail"),
]