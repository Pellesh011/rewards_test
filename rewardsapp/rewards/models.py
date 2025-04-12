from django.utils import timezone
from django.db import models

from accounts.models import CustomUser

class ScheduledReward(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    execute_at = models.DateTimeField()

    def __str__(self):
        return f"Reward of {self.amount} for {self.user.username} at {self.execute_at}"
    
class RewardLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reward of {self.amount} given to {self.user.username} at {self.given_at}"