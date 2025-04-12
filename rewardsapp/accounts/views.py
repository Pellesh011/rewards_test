from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    user_data = CustomUser.profile(user.id)
    serializer = UserSerializer(user_data, many=False)
    return Response(serializer.data, status=200)
    

