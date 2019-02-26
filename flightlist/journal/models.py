from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Entry(models.Model):
    title = models.CharField(max_length = 80)
    content = models.TextField(blank=True)
    date = models.DateField()
    image = models.CharField(max_length = 300)
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f'{self.title}'