from django import forms
from .models import BorrowRecord
class IssueBookForm(forms.ModelForm):
    class Meta:
        model=BorrowRecord
        fields=['member','book_copy','due_date']
        widgets={'due_date':forms.DateInput(attrs={'type':'date'})}
