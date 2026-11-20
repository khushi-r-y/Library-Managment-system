from rest_framework import serializers
from accounts.models import MemberProfile
class MemberSerializer(serializers.ModelSerializer):
    class Meta: model=MemberProfile; fields='__all__'
