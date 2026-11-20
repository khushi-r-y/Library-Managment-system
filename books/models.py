from django.db import models
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    def __str__(self): return self.name
class Book(models.Model):
    title=models.CharField(max_length=200)
    isbn=models.CharField(max_length=20,unique=True)
    author=models.CharField(max_length=150)
    publisher=models.CharField(max_length=150,blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='books')
    published_date=models.DateField(null=True,blank=True)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
class BookCopy(models.Model):
    STATUS=[('AVAILABLE','Available'),('ISSUED','Issued'),('MAINTENANCE','Maintenance')]
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='copies')
    accession_number=models.CharField(max_length=40,unique=True)
    status=models.CharField(max_length=12,choices=STATUS,default='AVAILABLE')
    def __str__(self): return f'{self.book.title} - {self.accession_number}'
