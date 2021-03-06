from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('numbles.accounts.urls', 'accounts')),
    url(r'^ledger/', include('numbles.ledger.urls', 'ledger')),
]
