from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example1.views.home', name='home'),
    url(r'^example/', include('ex.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
