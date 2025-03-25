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
    path('add-book-with-django-forms-dot-form/', views.add_book_with_django_forms_dot_form, name="add_book_with_django_forms_dot_form"),
    path('update-book-with-model-form/<int:book_id>/', views.update_book_with_model_form, name="update_book_with_model_form"),
    path('update-book-with-forms-dot-form/<int:book_id>/', views.update_book_with_forms_dot_form, name="update_book_with_forms_dot_form"),
    path('book/<int:book_pk>/', views.book_detail, name="book_detail"),
    path('confirm-delete/<int:book_pk>/', views.confirm_delete, name="confirm_delete"),
    path('delete-book/<int:book_id>/', views.delete_book, name="delete_book"),
]