from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.CharField(max_length=255)  # Or another appropriate field type
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'place_id')  # Ensure one favorite per user/place

    def __str__(self):
        return f"{self.user.username} - {self.place_id}"
