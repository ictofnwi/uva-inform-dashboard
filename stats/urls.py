from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^(?P<variable_name>[^/]+)/', get_variable_stats,
        name='variable_stats'),
]
