from rest_framework import serializers
from .models import BorrowRecord,Reservation,Fine
class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowRecord; fields='__all__'; read_only_fields=['issue_date','return_date','status']
    def create(self,validated_data):
        copy=validated_data['book_copy']
        if copy.status!='AVAILABLE': raise serializers.ValidationError({'book_copy':'This copy is not available.'})
        copy.status='ISSUED'; copy.save(update_fields=['status'])
        return super().create(validated_data)
class ReservationSerializer(serializers.ModelSerializer):
    class Meta: model=Reservation; fields='__all__'
class FineSerializer(serializers.ModelSerializer):
    class Meta: model=Fine; fields='__all__'
