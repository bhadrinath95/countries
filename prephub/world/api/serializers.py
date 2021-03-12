from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from world.models import Country, State, City
from django.contrib.admin.utils import lookup_field
from rest_framework import serializers

class CountriesListsSerializer(ModelSerializer):
    country_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Country
        fields = [
                'name',
                'country_url'
            ]
        
    def get_country_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
        
class StatesListsSerializer(ModelSerializer):
    state_url = serializers.SerializerMethodField()
    
    class Meta:
        model = State
        fields = [
                'name',
                'state_url'
            ]
    
    def get_state_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
    
class CitiesListsSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = [
                'name',
            ]