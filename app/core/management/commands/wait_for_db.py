import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command that waits for database to be available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        i = 0
        for i in range(10):
            try:
                connection.ensure_connection()
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        if i == 9:
            self.stdout.write(self.style.ERROR('Database is unavailable!'))
        else:
            self.stdout.write(self.style.SUCCESS('Database available!'))
