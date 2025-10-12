from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from UserInfo.models import UserInfo

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_info(request):
    info = UserInfo.objects.filter(user= request.user.id)
    if info:
        return Response('Info allready filled')
    else:
        UserInfo.objects.create(
            user = request.user,
            phone = request.data['phone'],
            dob = request.data['phone'],
        )