from itertools import count
from django.core.management.base import BaseCommand
import json
from gallery.models import Country

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('countries.json', 'rb') as f:
            data = json.load(f)

        for i in data:
            print(i)
            i = Country(name = i['country'])
            i.save()

