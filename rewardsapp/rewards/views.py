from datetime import timedelta

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.utils import timezone

from .tasks import execute_reward
from .models import RewardLog, ScheduledReward
from .serializers import RewardLogSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reward_list(request):
    rewards = RewardLog.objects.filter(user=request.user)
    serializer = RewardLogSerializer(rewards, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_reward(request):
    user = request.user
    now = timezone.now()
    last_request_time = now - timedelta(days=1)

    # Проверяем, делал ли пользователь запрос в течение последних 24 часов
    if ScheduledReward.objects.filter(user=user, created_at__gte=last_request_time).exists():
        return Response({"error": "Вы уже запросили награду в течение последних 24 часов."}, status=status.HTTP_400_BAD_REQUEST)

    # Создаем ScheduledReward, которая выполнится через 5 минут
    execute_at = now + timedelta(minutes=5)
    reward = ScheduledReward.objects.create(user=user, execute_at=execute_at, amount=5)
    execute_reward.apply_async((reward.id,), eta=execute_at)
    return Response({"message": "Награда успешно запрошена!", "execute_at": execute_at}, status=status.HTTP_201_CREATED)

