from django.conf import settings
from django.db import models
class MemberProfile(models.Model):
    ROLES=[('MEMBER','Member'),('LIBRARIAN','Librarian')]
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='member_profile')
    member_id=models.CharField(max_length=30,unique=True)
    phone=models.CharField(max_length=20,blank=True)
    department=models.CharField(max_length=100,blank=True)
    address=models.TextField(blank=True)
    role=models.CharField(max_length=12,choices=ROLES,default='MEMBER')
    def __str__(self): return f'{self.member_id} - {self.user.username}'
