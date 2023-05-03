from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ('title', 'author', )