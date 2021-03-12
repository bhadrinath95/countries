from django.shortcuts import render
from .models import Country, State, City
from django.views import View

# Create your views here.
class Country_View(View):
    template_name='list_display.html'
    def get(self, request):
        obj = Country.objects.all().order_by("name")
        return render(request,self.template_name,{"topic":"Country", "objects":obj})
    
class State_View(View):
    template_name='list_display.html'
    def get(self, request, country_slug):
        country_obj = Country.objects.get(slug=country_slug)
        obj = State.objects.filter(country=country_obj).order_by("name")
        return render(request,self.template_name,{"topic":"States of "+country_obj.name, "objects":obj})
    
class City_View(View):
    template_name='list_display.html'
    def get(self, request, country_slug, state_slug):
        state_obj = State.objects.get(slug=state_slug)
        obj = City.objects.filter(state=state_obj).order_by("name")
        return render(request,self.template_name,{"topic":"Cities of "+state_obj.name, "objects":obj})