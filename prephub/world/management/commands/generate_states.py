from django.core.management.base import BaseCommand
from django.utils import timezone
from geosky import geo_plug
from world.models import Country, State, City
import json
import unidecode

class Command(BaseCommand):
    help = 'Generates Countries'
   

    def handle(self, *args, **kwargs):
        PERMITTED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- " 
        try:
            data = geo_plug.all_Country_StateNames()
            data_lis = json.loads(data)
            countries = dict()
            for d in data_lis:
                countries.update(d)
            for country in countries.keys():
                for state in countries[country]:
                    if state and state.encode().decode('unicode_escape') != "N/A" and not State.objects.filter(name = "".join(c for c in unidecode.unidecode(state.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip()).exists():
                        cty = Country.objects.get(name=country)
                        
                        try:
                            State.objects.create(country = cty, name= "".join(c for c in unidecode.unidecode(state.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip())
                        except:
                            pass
                        self.stdout.write(self.style.SUCCESS("State '"+"".join(c for c in unidecode.unidecode(state.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip() +"' is added"))
                self.stdout.write(self.style.SUCCESS("States are successfully added for "+country))
        except Exception as err:
            self.stdout.write(self.style.ERROR('Error in creating states. ' % err))