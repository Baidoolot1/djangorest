from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth.models import User



@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializers = UserLoginSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        print(serializers.validated_data)
        # username = serializers.validated_data.get('username')
        # password = serializers.validated_data.get('password')
        user = authenticate(**serializers.validated_data)
        if not user:
            return Response(data={'message': 'User data are wrong!!'},
                            status=status.HTTP_403_FORBIDDEN)
        else:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializers = UserRegisterSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        return Response(status=status.HTTP_201_CREATED)


