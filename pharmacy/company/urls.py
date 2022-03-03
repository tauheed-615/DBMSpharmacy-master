from django.urls import include, path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^(?P<pharmacy_id>\d+)/add_stock/$', add_stock),
    url(r'^(?P<pharmacy_id>\d+)/get_stocks/$', get_stocks),
    url(r'^(?P<stock_id>\d+)/add_stock_item/$', add_stock_item),
    url(r'^(?P<stock_id>\d+)/get_stock_items/$', get_stock_items),
    url(r'^(?P<stock_id>\d+)/edit_stock/$', edit_stock),
    url(r'^(?P<stock_item_id>\d+)/edit_stock_item/$', edit_stock_item),
    url(r'^(?P<stock_id>\d+)/delete_stock/$', delete_stock),
    url(r'^(?P<stock_item_id>\d+)/delete_stock_item/$', delete_stock_item),
    url(r'^(?P<stock_id>\d+)/add_company/$', add_company),
    url(r'^(?P<company_id>\d+)/edit_company/$', edit_company),
    url(r'^(?P<company_id>\d+)/delete_company/$', delete_company)
]
