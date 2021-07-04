from django.conf.urls import url
from .views import *

urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^add_data$', add_data, name='add_data'),
    # url(r'^add_inverter$', add_inverter, name='add_inverter'),
    # url(r'^add_radiation$', add_radiation, name='add_radiation'),
    # url(r'^edit_pv/(?P<pk>\d+)$', edit_pv, name='edit_pv'),
    # url(r'^delete_pv/(?P<pk>\d+)$', delete_pv, name='delete_pv'),
    # url(r'^display_monthly$', display_monthlyRad, name='display_monthlyRad'),
]
