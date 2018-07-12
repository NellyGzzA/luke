from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserSerializer
from rest_framework_jwt.settings import api_settings

class UserCreate(APIView):
    """
    Creates a user
    """
    permission_classes = [ permissions.AllowAny ]

    def post(self, request):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                json = serializer.data
                json['token'] = token
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuth(APIView):
    """
    Authenticates user
    """

    def post(self,request):
        print(request.user.auth_token)
        print("INSIDEEEE")
