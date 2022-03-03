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
    r'^add_pharmacy/$',add_pharmacy),
    url(
    r'^(?P<pharmacy_id>\d+)/edit_pharmacy/$',edit_pharmacy),
    url(
    r'^get_pharmacys/$',get_pharmacys),
    url(
    r'^get_pharmacy/$',get_pharmacy),
    url(
    r'^get_user/(?P<username>.*)/$',get_user),
    url(
    r'^set_admin/(?P<username>.*)/$',set_admin),
    url(
    r'^set_user/(?P<username>.*)/$',set_user),
    url(
    r'^add_user/(?P<username>.*)/$',add_user),
    url(
    r'^add_user/$',add_users),
    url(
    r'^delete_user/(?P<username>.*)/$',delete_user),
    url(
    r'^add_user_admin/(?P<username>.*)/$',add_user_admin),
    url(
    r'^get_users/$',UserListView.as_view())


]
