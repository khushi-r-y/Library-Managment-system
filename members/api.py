from rest_framework import viewsets
from accounts.models import MemberProfile
from .serializers import MemberSerializer
class MemberViewSet(viewsets.ModelViewSet):
    queryset=MemberProfile.objects.select_related('user').all(); serializer_class=MemberSerializer
