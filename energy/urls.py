from django.conf.urls import url
from .views import *
from . import views
urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^energyGeneration/ (?P<month>\d+)$', energyGeneration, name='energyGeneration'),
     url(r'^display_monthly$', display_monthlyRad, name='display_monthlyRad'),
     url(r'^energyCall$', energyCall, name='energyCall'),

]
