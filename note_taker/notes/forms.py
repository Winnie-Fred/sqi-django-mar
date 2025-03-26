from django import forms

from .models import Note, Category

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "category"]


class SearchNotesForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)

class FilterByCategory(forms.Form):
    category = forms.ChoiceField(choices=Category.choices, required=False)