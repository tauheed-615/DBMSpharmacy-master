from django.urls import include, path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^(?P<pharmacy_id>\d+)/add_drug/$', add_drug),
    url(r'^(?P<pharmacy_id>\d+)/check_drug_expiry/$', get_drug_expiry_alert),
    url(r'^(?P<drug_id>\d+)/edit_drug/$', edit_drug),
    url(r'^(?P<drug_id>\d+)/delete_drug/$', delete_drug),
    url(r'^(?P<pharmacy_id>\d+)/get_drugs/$', get_drugs),
    url(r'^(?P<pharmacy_id>\d+)/get_drug/(?P<drug_id>\d+)$', get_drug)
]
