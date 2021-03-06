from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.template.response import SimpleTemplateResponse

from . import views


def login_(request, **kwargs):
    """Adds template variables to the login view."""
    response = login(request, **kwargs)
    if isinstance(response, SimpleTemplateResponse):
        response.context_data.update({
            'title': 'Login',
            'fullscreen': True,
        })
    return response


urlpatterns = [
    url(r'^login/$', login_, {'template_name': 'accounts/pages/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'accounts:login'}, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]
