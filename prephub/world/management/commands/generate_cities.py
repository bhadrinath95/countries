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
                    if state and state.encode().decode('unicode_escape') != "N/A" and State.objects.filter(name = "".join(c for c in unidecode.unidecode(state.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip()).exists():
                        state_obj = State.objects.get(name = "".join(c for c in unidecode.unidecode(state.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip())
                        cities_data = geo_plug.all_State_CityNames(state)
                        cities_data_lis = json.loads(cities_data)
                        cities = dict()
                        for d in cities_data_lis:
                            cities.update(d)
                        for st in cities.keys():
                            ctys = cities[st]
                            for cty in ctys:
                                if cty and cty.encode().decode('unicode_escape') != "N/A" and not City.objects.filter(name = "".join(c for c in unidecode.unidecode(cty.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip()).exists():
                                    try:
                                        City.objects.create(state = state_obj, name= "".join(c for c in unidecode.unidecode(cty.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip())
                                        self.stdout.write(self.style.SUCCESS("City '"+"".join(c for c in unidecode.unidecode(cty.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip() +"' is added"))
                                    except:
                                        pass
                        self.stdout.write(self.style.SUCCESS("Cities are successfully added for "+"".join(c for c in unidecode.unidecode(state.encode().decode('unicode_escape')) if c in PERMITTED_CHARS).lower().capitalize().rstrip()))
        except Exception as err:
            self.stdout.write(self.style.ERROR('Error in creating states. ' % err))