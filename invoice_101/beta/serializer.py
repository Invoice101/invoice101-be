from rest_framework.serializers import ModelSerializer

from .models import BetaSubscription


class BetaSubscriptionSerializer(ModelSerializer):
    class Meta:
        model = BetaSubscription
        fields = '__all__'
