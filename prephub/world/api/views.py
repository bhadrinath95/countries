from rest_framework.generics import (
    ListAPIView, 
    )
from .serializers import CountriesListsSerializer, StatesListsSerializer, CitiesListsSerializer
from world.models import Country, State, City
from .pagination import ( 
    PageNumberPagination
    )
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountriesListsSerializer
    pagination_class = PageNumberPagination 
    
class StateListAPIView(ListAPIView):
    serializer_class = StatesListsSerializer
    pagination_class = PageNumberPagination 
    
    def get_queryset(self, *args, **kwargs):
        country_obj = Country.objects.get(slug=self.kwargs.get("country_slug"))
        query_list = State.objects.filter(country=country_obj).order_by("name")
        return query_list
    
class CityListAPIView(ListAPIView):
    serializer_class = CitiesListsSerializer
    pagination_class = PageNumberPagination 
    
    def get_queryset(self, *args, **kwargs):
        state_obj = State.objects.get(slug=self.kwargs.get("state_slug"))
        query_list = City.objects.filter(state=state_obj).order_by("name")
        return query_list
