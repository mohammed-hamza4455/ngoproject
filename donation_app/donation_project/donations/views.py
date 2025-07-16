from rest_framework import viewsets
from .models import Donation
from .serializers import DonationSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all().order_by('-donated_at')
    serializer_class = DonationSerializer
