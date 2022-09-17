from django.http import Http404
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer
from .serializers import LoginSerializer
from .serializers import RegistrationSerializer

"""
class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'token': serializer.data.get('token', None), }, status=status.HTTP_201_CREATED,)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
"""

class CurrentUserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        if not self.request.user.is_authenticated:
            raise Http404

        return self.request.user