from community.models import Community
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommunityViewSerializer, CommunityListViewSerializer

class CommunityView(APIView):
    def get(self, request):
        community = Community.objects.all()
        serializer = CommunityListViewSerializer(community, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        print(request.user)
        serializer = CommunityViewSerializer(data=request.data)
        print(request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class CommunityDetailView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CommentView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CommentDetailView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class LikeView(APIView):


    def post(self, request):
        pass

