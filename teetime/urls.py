from django.conf.urls import url
from views import get_teeTime, requested_teeTime

urlpatterns = [
    url(r'^$', get_teeTime, name='tee'),
    url(r'^$', requested_teeTime, name='request'),
]