from django.db import models

# Create your models here.

class Activity(models.Model):
    activity_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.activity_text
