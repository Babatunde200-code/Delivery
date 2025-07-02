from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TravelPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='travel_plans')
    origin_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    departure_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} travels from {self.origin_country} to {self.destination_country}"

