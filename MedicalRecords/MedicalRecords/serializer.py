from rest_framework import serializers

class UserInfoSerialazer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)
