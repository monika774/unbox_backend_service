from django.db import models
from django.utils import timezone

class SpeedData(models.Model):
    """   Model to store speed data points  """
    speed = models.FloatField()  
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Speed Data"

    def __str__(self):
        return f"Speed: {self.speed} at {self.timestamp}"
    
