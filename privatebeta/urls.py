from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'views.invite', name='privatebeta_invite'),
    url(r'^sent/$', 'views.sent', name='privatebeta_sent'),
)
