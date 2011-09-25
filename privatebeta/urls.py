from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^$', views.invite, name='privatebeta_invite'),
    url(r'^sent/$', views.sent, name='privatebeta_sent'),
)
