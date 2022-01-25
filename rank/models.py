from django.db import models

# Create your models here.
class rank_data(models.Model):
    user_id = models.TextField()
    user_score = models.IntegerField()
    user_name = models.TextField()
    class Meta:
        ordering = ['-user_score']