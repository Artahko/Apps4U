from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    YEAR_CHOICES = [
        (1, 'Перший курс'),
        (2, 'Другий курс'),
        (3, 'Третій курс'),
        (4, 'Четвертий курс'),
    ]

    MAJOR_CHOICES = [
        ('CS', "Комп'ютерні науки"),
        ('RO', 'Робототехніка'),
        ('DA', 'ІТ та Аналітика Рішень'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500,blank=True)
    icon = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')

    major = models.CharField(
        max_length=2,
        choices=MAJOR_CHOICES,
        default='NONE'
    )
    year_of_study = models.IntegerField(
        choices=YEAR_CHOICES,
        default=0,
        verbose_name="Current Course Year"
    )


    def __str__(self):
        return f'{self.user.username} - Profile'
