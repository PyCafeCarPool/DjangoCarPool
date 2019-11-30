from django.conf.urls import url
from . import views

app_name='rideshare'

urlpatterns=[
    url(r'^$', views.retrieve_kids_drivers,
    name='retrieve_kids_drivers'),

]
