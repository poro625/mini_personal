from rest_framework import serializers
from community.models import Community


class CommunityViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class CommunityListViewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = ("pk","user", "title", "image","content")
    
    def get_user(self,obj):
        return obj.user.email

class CommunityCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ("title", "image","content")
