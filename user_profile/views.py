# user_account/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serialiser import ProfileSerializer

class ProfileUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
