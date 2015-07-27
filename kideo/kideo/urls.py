import os

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url('media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': 'media/'}),
        
    url(r'', include('feincms.contrib.preview.urls')),
        url(r'^gallery/', include('gallery.urls')),
    url(r'', include('feincms.urls')),


) + staticfiles_urlpatterns()

