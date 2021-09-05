from django.conf.urls import url
from .views import *
from . import views
urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^add_pv$', add_pv, name='add_pv'),

]
