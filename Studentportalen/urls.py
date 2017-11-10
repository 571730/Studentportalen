from django.conf.urls import url
from . import views

app_name = 'Studentportalen'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^emner/$', views.emner, name='emner'),
    url(r'^fag/+(?P<emne_id>[0-9]+)/$', views.fag, name='fag'),
    url(r'^logg_inn/$', views.login_view, name='login_user'),
    url(r'^logg_ut/$', views.logout_view, name='logout_user'),
    url(r'^registrering/$', views.register, name='registrering'),
]