from rest_framework import generics, permissions
from .models import TravelPlan
from .serializers import TravelPlanSerializer

class TravelPlanCreateView(generics.CreateAPIView):
    serializer_class = TravelPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
