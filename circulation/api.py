from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import BorrowRecord,Reservation,Fine
from .serializers import BorrowRecordSerializer,ReservationSerializer,FineSerializer
class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset=BorrowRecord.objects.select_related('member','book_copy').all()
    serializer_class=BorrowRecordSerializer
    @action(detail=True,methods=['post'])
    def return_book(self,request,pk=None):
        record=self.get_object()
        if record.status not in ['ISSUED','OVERDUE']: raise ValidationError('Already returned.')
        record.mark_returned()
        return Response(BorrowRecordSerializer(record).data)
class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.select_related('member','book').all(); serializer_class=ReservationSerializer
class FineViewSet(viewsets.ModelViewSet):
    queryset=Fine.objects.select_related('borrow_record').all(); serializer_class=FineSerializer
