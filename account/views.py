from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.serializers import UserRegistrationSerializer, LoginSerializer
from django.contrib.auth import authenticate


class UserRegisterView(APIView):
    def post(self, request, format=None):

        #!  send data
        serializer = UserRegistrationSerializer(data=request.data)

        #!  check valid data
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Register successfull"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")

            user = authenticate(email=email, password=password)

            if user is not None:
                return Response({"message": "Login Success"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": {"non_field_errors": ["Email or Password not found"]}}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)