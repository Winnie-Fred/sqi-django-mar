from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path('all-books/', views.all_books, name="all_books"),
    path('book/<int:book_id>/', views.book_detail, name="book_detail"),
]