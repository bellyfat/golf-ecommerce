"""golf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Accounts import urls as accounts_urls
from home.views import get_index
from products import urls as products_urls
from cart import urls as cart_urls
from categories import urls as categories_urls
from settings import MEDIA_ROOT
from django.views import static
from blog import urls as blog_urls
from home.views import handle_message_form
from home.views import get_teeTime


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^user/', include(accounts_urls)),
    url(r'^$', get_index, name='index'),
    url(r'^products/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^categories/', include(categories_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^message/', handle_message_form, name='send_message'),
    url(r'^teetime/', get_teeTime, name='teetime'),
]
