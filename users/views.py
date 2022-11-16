from users.models import User
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer, UserUpdateSerializer
from rest_framework.generics import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

class UserView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView): #프로필 편집    

    def get(self, request, user_id): #프로필 조회
        user = get_object_or_404(User, id=user_id)
        serializer = UserUpdateSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id): # 프로필 수정
        user = User.objects.get(id=user_id)
        serializer = UserUpdateSerializer(user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, user_id): # 프로필 삭제
        user = User.objects.get(id=user_id)
        return



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer