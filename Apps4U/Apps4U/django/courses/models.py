from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    course_id = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"


class Activity(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    activity_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.activity_text

class Material(models.Model):
    activity = models.ForeignKey(Activity, related_name='materials', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    upload = models.FileField(upload_to='activity_materials/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.question}"


class Comment(models.Model):
    post = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
