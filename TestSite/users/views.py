from os import execlp
from django.conf import settings
from django.http import response
from rest_framework import permissions
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from .models import User
import jwt
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.signals import user_logged_in



# Create your views here.
class CreateUserViewAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(requsets):
    try:
        login = requsets.data['login']
        password = requsets.data['password']

        user = User.objects.get(login=login,password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload,settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = (user.login)
                user_details['token'] = token
                #user_logged_in.send(sender=user.__class__,requset=requsets,user=user)
                return Response(user_details,status=status.HTTP_200_OK)
            except Exception as ex:
                raise ex
        else:
            respons = {'error':'account deactiveted'}
            return Response(respons,status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        respons = {'error':'bad login or password'}
        return Response(respons)



