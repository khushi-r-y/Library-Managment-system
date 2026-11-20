from django.contrib import admin
from .models import BorrowRecord,Reservation,Fine
admin.site.register(BorrowRecord)
admin.site.register(Reservation)
admin.site.register(Fine)
