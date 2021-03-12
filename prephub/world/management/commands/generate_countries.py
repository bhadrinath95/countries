from django.core.management.base import BaseCommand
from django.utils import timezone
from geosky import geo_plug
from world.models import Country, State, City
import json

class Command(BaseCommand):
    help = 'Generates Countries'
    def handle(self, *args, **kwargs):
        try:
            data = geo_plug.all_Country_StateNames()
            data_lis = json.loads(data)
            countries = dict()
            for d in data_lis:
                countries.update(d)
            for country in countries.keys():
                print(country)
                if not Country.objects.filter(name = country).exists():
                    Country.objects.create(name= country)
                
            self.stdout.write(self.style.SUCCESS("Countries are successfully added"))
        except Exception as err:
            self.stdout.write(self.style.ERROR('Error in creating countries. ' % err))