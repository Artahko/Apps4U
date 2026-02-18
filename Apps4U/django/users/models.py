from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    YEAR_CHOICES = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    ]

    MAJOR_CHOICES = [
        ('CS', 'Computer Science'),
        ('RO', 'Robotics'),
        ('DA', 'IT and Decision Analytics'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=500,blank=True)
    about = models.TextField(max_length=500,blank=True)
    icon = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')

    major = models.CharField(
        max_length=2,
        choices=MAJOR_CHOICES,
        default='CS'
    )
    year_of_study = models.IntegerField(
        choices=YEAR_CHOICES,
        default=1,
        verbose_name="Current Course Year"
    )


    def __str__(self):
        return f'{self.user.username} - Profile'
