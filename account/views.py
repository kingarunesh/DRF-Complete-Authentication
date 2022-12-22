from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.serializers import UserRegistrationSerializer


class UserRegisterView(APIView):
    def post(self, request, format=None):

        #!  send data
        serializer = UserRegistrationSerializer(data=request.data)

        #!  check valid data
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Register successfull"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    