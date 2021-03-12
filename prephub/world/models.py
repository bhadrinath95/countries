from django.db import models
from django.utils.text import slugify
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_api_url(self, request=None):
        return api_reverse('world-api:state', kwargs={'country_slug': self.slug}, request=request)

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_api_url(self, request=None):
        return api_reverse('world-api:city', kwargs={'country_slug': self.country.slug, 'state_slug': self.slug}, request=request)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name