from rest_framework import serializers
from UserInfo.models import UserInfo

class UserInfoSerialazer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

        def create(self, validated_data):
            return UserInfo.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            info = UserInfo.objects.get(id=instance)
            info.prefix = validated_data.get("prefix", info.prefix)
            info.f_name = validated_data.get("f_name", info.f_name)
            info.m_name = validated_data.get("m_name", info.m_name)
            info.l_name = validated_data.get("l_name", info.l_name)
            info.dob = validated_data.get("dob", info.dob)
            info.address_1 = validated_data.get("address_1", info.address_1)
            info.address_2 = validated_data.get("address_2", info.address_2)
            info.city = validated_data.get("city", info.city)
            info.state = validated_data.get("state", info.state)
            info.zip_code = validated_data.get("zip_code", info.zip_code)
            return info
