from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','isbn','author','publisher','category','published_date','description']
        widgets={'published_date':forms.DateInput(attrs={'type':'date'})}
