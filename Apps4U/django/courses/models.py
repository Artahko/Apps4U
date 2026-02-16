from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    course_id = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"

class FAQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=200)
    answear = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.question}"
