from django import forms

from .models import Book
from authors.models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "number_of_pages", "published_on", "cover_image"]


class BookManualForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput())
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    number_of_pages = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}))
    # published_on = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    published_on = forms.DateField(widget=forms.SelectDateWidget())
    cover_image = forms.ImageField(required=False, widget=forms.ClearableFileInput())