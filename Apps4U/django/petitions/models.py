from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Petition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    @property
    def days_remaining(self):
        expiry = self.created_at + timedelta(days=30)
        remaining = expiry - timezone.now()
        return max(0, remaining.days)



class Vote(models.Model):
    VOTE_CHOICES = [
        (1, 'Like'),
        (-1, 'Dislike'),
    ]
    petition = models.ForeignKey(Petition, related_name="votes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        # not liking multiple times
        unique_together = ('petition', 'user')
