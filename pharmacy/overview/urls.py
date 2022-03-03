from django.urls import include, path
from django.conf.urls import url, include
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from .views import *

urlpatterns = [

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('drug/', include('drug.urls')),
    path('stock/', include('company.urls')),
    url(r'^rest-auth/facebook/connect/$', FacebookLogin.as_view(), name='fb_connect'),
    url(
        r'^socialaccounts/$',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    url(
        r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    ),
    url(
    r'^add_pharmacy/$',add_pharmacy)


]
