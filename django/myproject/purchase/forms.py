from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    book_id = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    user_id = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 100px', 'class': 'form-control'}))

    class Meta:
        model = Purchase
        fields = ('book_id', 'user_id', )