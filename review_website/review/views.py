from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Book, Review
from .forms import ReviewForm

from utils.login_decorator import custom_login_required, user_is_review_owner

# Create your views here.
def all_books(request):
    return render(request, "review/all-books.html", {"books": Book.objects.all()})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    url = reverse('review:book_detail', kwargs={"book_id": book_id})
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, f"You need to be logged in to leave a review for {book.title}")
            return redirect('users:log_in')
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.added_by = request.user
            review.save()

    return render(request, "review/book-detail.html", {"book": book, "form": form, "url": url})


@custom_login_required
@user_is_review_owner("edit")
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = ReviewForm(instance=review)
    url = reverse('review:edit_review', kwargs={"review_id": review_id})
    current_time = timezone.now()
    time_diff = current_time - review.added_on
    EDIT_REVIEW_LIMIT_IN_SECONDS = 5 * 60
    if time_diff.seconds > EDIT_REVIEW_LIMIT_IN_SECONDS:
        messages.error(request, "You can no longer edit this review. It has been 5 minutes.")
        return redirect(reverse('review:book_detail', kwargs={"book_id": review.book.id}))

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your review was edited successfully")
            return redirect(reverse('review:book_detail', kwargs={"book_id": review.book.id}))

    context = {"form": form, "url": url}
    return render(request, "review/edit-review.html", context)

@custom_login_required
@user_is_review_owner("delete")
def confirm_delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, "review/confirm-delete-review.html", {"review": review})

@custom_login_required
@user_is_review_owner("delete")
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        review.delete()
        messages.success(request, f"Your review was deleted successfully")

    return redirect(reverse('review:book_detail', kwargs={"book_id": review.book.id}))
