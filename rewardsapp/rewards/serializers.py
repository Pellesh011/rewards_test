from rest_framework import serializers
from .models import RewardLog

class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ['id', 'user', 'amount', 'given_at']  # Укажите поля, которые хотите вернуть
