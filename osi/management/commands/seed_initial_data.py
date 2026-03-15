from django.core.management import call_command
from django.core.management.base import BaseCommand

from osi.models import Layer


class Command(BaseCommand):
    help = "Seed initial app data if database is empty"

    def handle(self, *args, **kwargs):
        if Layer.objects.exists():
            self.stdout.write(self.style.WARNING("Data already exists. Skipping seed."))
            return

        self.stdout.write("No layer data found. Loading initial sample data...")
        call_command("load_sample_data")
        self.stdout.write(self.style.SUCCESS("Initial data seeded successfully."))
