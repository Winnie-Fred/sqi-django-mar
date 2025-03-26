from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from django.urls import reverse

from .models import Note
from .forms import NoteForm, SearchNotesForm, FilterByCategory

# Create your views here.
def fetch_notes(request):
    notes = Note.objects.all()
    print(request.GET)
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

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "notes/note.html", {"note": note})

def create_note(request):
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:fetch_notes')

    context = {
        "form": form
    }
    return render(request, "notes/create-note.html", context)


def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
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

def confirm_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "notes/confirm-delete.html", {"note": note})


def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == "POST":
        note.delete()
        return redirect("notes:fetch_notes")

    return HttpResponseNotAllowed(["POST"])