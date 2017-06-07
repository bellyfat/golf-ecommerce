from django.conf.urls import url
from .views import get_teeTime

urlpatterns = [
    url(r'^$', get_teeTime, name='teetime.html'),
    url(r'teetime/$',teetimeMessage, name='teetimeMessage.html'),
]

