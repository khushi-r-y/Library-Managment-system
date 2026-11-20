from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import BorrowRecord
from .forms import IssueBookForm
@staff_member_required
def circulation_list(request):
    records=BorrowRecord.objects.select_related('member__user','book_copy__book').order_by('-issue_date')
    for r in records.filter(status='ISSUED',due_date__lt=timezone.localdate()):
        r.status='OVERDUE'; r.save(update_fields=['status'])
    return render(request,'circulation/circulation_list.html',{'records':records})
@staff_member_required
def issue_book(request):
    form=IssueBookForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        record=form.save(commit=False)
        if record.book_copy.status!='AVAILABLE': form.add_error('book_copy','This copy is not available.')
        else:
            record.book_copy.status='ISSUED'; record.book_copy.save(update_fields=['status'])
            record.save(); return redirect('circulation_list')
    return render(request,'circulation/issue_form.html',{'form':form})
@staff_member_required
def return_book(request,pk):
    record=get_object_or_404(BorrowRecord,pk=pk)
    if record.status in ['ISSUED','OVERDUE']: record.mark_returned()
    return redirect('circulation_list')
