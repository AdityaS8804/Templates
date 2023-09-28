from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serielizers import RegisterUserSerielizer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
from rest_framework import status
class CustomUserCreate(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        reg_serielizer=RegisterUserSerielizer(data=request.data)
        if reg_serielizer.is_valid():
            newuser=reg_serielizer.save()
            if newuser:
                print(newuser.user_name)
                return Response(
                    {
                        "User":str(newuser),
                        "data":request.data,
                        "ser":reg_serielizer.data
                    },status=status.HTTP_201_CREATED)
        return Response(reg_serielizer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlacklistTokenView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)