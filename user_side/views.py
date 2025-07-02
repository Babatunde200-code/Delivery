from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import SignupSerializer


User = get_user_model()

class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
