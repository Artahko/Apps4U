from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    course_id = models.CharField(max_length=10, unique=True) # e.g., CS101
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course_id}: {self.title}"
