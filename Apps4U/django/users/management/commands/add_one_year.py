from django.core.management.base import BaseCommand
from users.models import Profile

class Command(BaseCommand):
    help = 'Adds one year to students year of study, 4-th year students get deleted'

    def handle(self, *args, **kwargs):
        Profile.objects.filter(year_of_study=4).delete()

        for year in [3, 2, 1]:
            students = Profile.objects.filter(year_of_study=year)

            students.update(year_of_study = year + 1)
