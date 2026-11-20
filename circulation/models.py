from django.db import models
from django.utils import timezone
from accounts.models import MemberProfile
from books.models import BookCopy,Book
class BorrowRecord(models.Model):
    STATUS=[('ISSUED','Issued'),('RETURNED','Returned'),('OVERDUE','Overdue')]
    member=models.ForeignKey(MemberProfile,on_delete=models.PROTECT,related_name='borrow_records')
    book_copy=models.ForeignKey(BookCopy,on_delete=models.PROTECT,related_name='borrow_records')
    issue_date=models.DateTimeField(default=timezone.now)
    due_date=models.DateField()
    return_date=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=10,choices=STATUS,default='ISSUED')
    def __str__(self): return f'{self.member} - {self.book_copy}'
    def mark_returned(self):
        self.return_date=timezone.now(); self.status='RETURNED'
        self.save(update_fields=['return_date','status'])
        self.book_copy.status='AVAILABLE'; self.book_copy.save(update_fields=['status'])
        late=max((self.return_date.date()-self.due_date).days,0)
        if late: Fine.objects.get_or_create(borrow_record=self,defaults={'amount':late*5})
class Reservation(models.Model):
    STATUS=[('PENDING','Pending'),('FULFILLED','Fulfilled'),('CANCELLED','Cancelled')]
    member=models.ForeignKey(MemberProfile,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    reservation_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS,default='PENDING')
class Fine(models.Model):
    borrow_record=models.OneToOneField(BorrowRecord,on_delete=models.CASCADE,related_name='fine')
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    paid=models.BooleanField(default=False)
    payment_date=models.DateTimeField(null=True,blank=True)
