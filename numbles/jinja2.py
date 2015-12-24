"""
Customize the Jinja2 environment
"""

from __future__ import absolute_import
from hashlib import md5
from os.path import basename

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.template.defaultfilters import linebreaksbr
from django.utils.timezone import now, template_localtime
from jinja2 import Environment
from widget_tweaks.templatetags.widget_tweaks import add_class, widget_type


def param(request, key, valid, default=None):
    """
    Retrieve the current sort field from the query string. Only the provided
    fields are accepted.
    """
    value = request.GET.get(key, default)
    return value if value in valid else default


def qs(request, **kwargs):
    """
    Output the query string for the current page with the specified additions
    and/or modifications.
    """
    get = request.GET.copy()
    for k, v in kwargs.items():
        get[k] = v
    return get.urlencode()


def environment(**kwargs):
    """
    Add some utility functions to the Jinja2 environment
    """
    env = Environment(**kwargs)
    env.filters.update({
        'add_class': add_class,
        'widget_type': widget_type,
    })
    env.globals.update({
        'basename': basename,
        'linebreaksbr': linebreaksbr,
        'localtime': lambda x: template_localtime(x).strftime('%Y-%m-%d %H:%M:%S'),
        'md5': lambda x: md5(x).hexdigest(),
        'now': now,
        'param': param,
        'qs': qs,
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
