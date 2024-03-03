from django.db import models
from datetime import datetime
import datetime as dt
# Create your models here.

class Container(models.Model):
    """Representaition of the Container table"""
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    volume = models.IntegerField()
    expiration_date = models.DateTimeField(default=(datetime.now()+dt.timedelta(days=1080)))
    location = models.CharField(max_length=100)

    class Meta:
        db_table = 'containers'
