from django.urls import path, re_path
from .views import Country_View, State_View, City_View
urlpatterns=[
    re_path('(?P<country_slug>[\w-]+)/(?P<state_slug>[\w-]+)/cities', City_View.as_view(), name = 'city'),
    re_path('(?P<country_slug>[\w-]+)/states', State_View.as_view(), name = 'state'),
    path('countries',Country_View.as_view(),name='country'),
]