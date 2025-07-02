from django.urls import path
from .views import TravelPlanCreateView

urlpatterns = [
    path('travels/', TravelPlanCreateView.as_view(), name='create-travel'),
]

