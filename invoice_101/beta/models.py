from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class BetaSubscription(TimeStampedModel):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500, unique=True)

    class Meta:
        verbose_name = 'Beta Subscription'
        verbose_name_plural = 'Beta Subscriptions'

    def __str__(self):
        return f"{self.name} - {self.email}"
