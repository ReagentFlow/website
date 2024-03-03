from django.db import models
from datetime import timedelta
from django.utils import timezone


# Create your models here.

class Container(models.Model):
    """Representaition of the Container table"""
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    volume = models.FloatField()
    expiration_date = models.DateField()
    location = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.expiration_date = timezone.now().date() + timedelta(days=3*365)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'containers'
