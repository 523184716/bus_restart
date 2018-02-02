from django.conf.urls import  url
from views import  *
urlpatterns = [
    url(r'^index/',index,name="index"),
    url(r'^service/(?P<project_name>\w+)',service,name="service")
]