from django.urls import path, re_path
from .views import CountryListAPIView, StateListAPIView, CityListAPIView

app_name = 'world'

urlpatterns = [
    re_path('countries/(?P<country_slug>[\w-]+)/(?P<state_slug>[\w-]+)', CityListAPIView.as_view(), name = 'city'),
    re_path('countries/(?P<country_slug>[\w-]+)', StateListAPIView.as_view(), name='state'),
    path('countries', CountryListAPIView.as_view(), name='country'),
]
