from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from UserInfo.models import User, UserInfo
from UserInfo.serializer import UserInfoSerialazer

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    data = request.data
    if User.objects.filter(email= data['email']).exists():
        Response({"detail": "User with same email allready exists!"}, status=400)
    user = User.objects.create_user(email=data['email'], password=data['password'])
    data['user']= user.id
    serialized =  UserInfoSerialazer(data=data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)
    return Response(serialized.errors, status=400)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def update_user(reqest):
    serialized = UserInfoSerialazer(UserInfo.objects.get(user=reqest.user.id), data=reqest.data, partial=True)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)
    return Response(serialized.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_user_info(request):
    info = UserInfoSerialazer(UserInfo.objects.get(user=request.user.id))
    return Response(info.data)