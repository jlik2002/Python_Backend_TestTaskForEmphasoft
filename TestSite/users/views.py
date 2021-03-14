from os import execlp, stat
from django.conf import settings
from django.db import models
from django.http import response
from rest_framework import permissions, serializers
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import permission_classes
from .models import User
import jwt
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.signals import user_logged_in




class CreateUserViewAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetMe(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request,*args,**kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
class Change(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def put(self, request,*args,**kwargs):
        serializer_data = request.data
        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class Remove(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def post(self, request,*args,**kwargs):
        try:
            id_for_remove = request.data.get('id')
            user_for_remove = User.objects.get(id=id_for_remove)
            serializer = UserSerializer(user_for_remove,data={'is_active':False},partial=True)
            #serializer.object.is_active = False
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'this id not found'}, status=status.HTTP_404_NOT_FOUND)

def HiPage(requests):
    return response.HttpResponse('Hello, test site for CRUD')

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(requsets):
    try:
        login = requsets.data['login']
        password = requsets.data['password']

        user = User.objects.get(login=login,password=password)
        if user.is_active:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload,settings.SECRET_KEY)
                user_details = {}
                user_details['login'] = (user.login)
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



