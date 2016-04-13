from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^api/$', views.api, name='api'),
    url(r'^list/$', views.list, name='list'),
    url(r'^(?P<brew_id>[0-9]+)/$', views.api, name='api'),
]
