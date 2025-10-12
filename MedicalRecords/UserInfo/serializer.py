from rest_framework import serializers
from UserInfo.models import UserInfo

class UserInfoSerialazer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

        def create(self, validated_data):
            return UserInfo.objects.create(**validated_data)
