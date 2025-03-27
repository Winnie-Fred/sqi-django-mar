from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Note
from .forms import NoteForm, SearchNotesForm, FilterByCategory

# Create your views here.

def home(request):
    return render(request, "notes/home.html")

@login_required
def fetch_notes(request):
    notes = Note.objects.filter(added_by=request.user)
    search_form = SearchNotesForm(request.GET)

    if search_form.is_valid():
        title = search_form.cleaned_data.get('title')
        if title:
            notes = notes.filter(title__icontains=title)

    filter_form = FilterByCategory(request.GET)

    if filter_form.is_valid():
        category = filter_form.cleaned_data.get('category')
        if category:
            notes = notes.filter(category=category)

    context = {
        "notes": notes,
        "filter_form": filter_form,
    }
    return render(request, "notes/notes.html", context)


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.added_by:
        messages.error(request, "You do not have permission to view that note")
        return redirect("notes:home")
    return render(request, "notes/note.html", {"note": note})


@login_required
def create_note(request):
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.added_by = request.user
            note.save()
            return redirect('notes:fetch_notes')

    context = {
        "form": form
    }
    return render(request, "notes/create-note.html", context)


@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.added_by:
        messages.error(request, "You do not have permission to edit that note")
        return redirect("notes:home")
    
    form = NoteForm(instance=note)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse('notes:note_detail', kwargs={"note_id": note_id}))

    context = {
        "form": form,
        "note": note,
    }
    return render(request, "notes/edit-note.html", context)

@login_required
def confirm_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.added_by:
        messages.error(request, "You do not have permission to delete that note")
        return redirect("notes:home")
    
    return render(request, "notes/confirm-delete.html", {"note": note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.added_by:
        messages.error(request, "You do not have permission to delete that note")
        return redirect("notes:home")
    

    if request.method == "POST":
        note.delete()
        return redirect("notes:fetch_notes")

    return HttpResponseNotAllowed(["POST"])