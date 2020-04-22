from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return f'{self.name}'
