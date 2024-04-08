from django.core.management.base import BaseCommand
from job.fetch_data import fetch_jobs

class Command(BaseCommand):
    help = 'Get Job Data from adzuna each 24 hours'

    def handle(self, *args, **kwargs):

        print("========= fetch job data task ========")
        fetch_jobs()
        self.stdout.write(self.style.SUCCESS('Successfully ran task'))