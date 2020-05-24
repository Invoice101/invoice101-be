from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Subscription(TimeStampedModel):
    email = models.EmailField(max_length=500, unique=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return f"{self.email}"
