from celery import shared_task
from django.db.models import F
from .models import ScheduledReward, RewardLog, CustomUser

@shared_task
def execute_reward(reward_id):
    try:
        reward = ScheduledReward.objects.get(id=reward_id)
        CustomUser.objects.filter(id=reward.user.id).update(coins=F('coins') + reward.amount)
        RewardLog.objects.create(user=reward.user, amount=reward.amount)
        print(f"Награда для пользователя {reward.user.username} выполнена!")
    except ScheduledReward.DoesNotExist:
        print("Награда не найдена.")
