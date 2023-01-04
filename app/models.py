from django.db import models

class Outbreak(models.Model):
    satellite = models.TextField(default=None)
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    longitude = models.DecimalField(max_digits=7, decimal_places=5)
    date = models.DateField(auto_now=False, auto_now_add=False)
    city = models.TextField()
    state = models.TextField()
    
    class Meta:
        unique_together = ['latitude','longitude','date']
        indexes = [models.Index(fields=['latitude','longitude','date'])]

    def serialize(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "date": self.date,
            "city": self.city,
            "state": self.state,
        }