from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path('all-books/', views.all_books, name="all_books"),
    path('book/<int:book_id>/', views.book_detail, name="book_detail"),
    path('edit-review/<int:review_id>/', views.edit_review, name="edit_review"),
    path('confirm-delete-review/<int:review_id>/', views.confirm_delete_review, name="confirm_delete_review"),
    path('delete-review/<int:review_id>/', views.delete_review, name="delete_review"),
]