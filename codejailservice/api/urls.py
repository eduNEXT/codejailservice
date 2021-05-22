"""
Api URLs.
"""
from django.conf.urls import include, url

app_name = 'api'
urlpatterns = [
    url(r'v0/', include(('codejailservice.api.v0.urls', app_name), namespace='v0')),
]
