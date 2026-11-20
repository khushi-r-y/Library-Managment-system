from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
@staff_member_required
def book_list(request):
    q=request.GET.get('q','')
    books=Book.objects.select_related('category')
    if q: books=books.filter(title__icontains=q) | books.filter(author__icontains=q) | books.filter(isbn__icontains=q)
    return render(request,'books/book_list.html',{'books':books,'query':q})
@staff_member_required
def book_create(request):
    form=BookForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save(); return redirect('book_list')
    return render(request,'books/book_form.html',{'form':form})
