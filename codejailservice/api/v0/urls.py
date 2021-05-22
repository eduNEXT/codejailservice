"""
Codejail Service  API URL Configuration
"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^code-exec$',
        views.CodeExec.as_view(),
        name='code-exec',
    ),
]