from django.conf.urls import url, patterns, include


urlpatterns = patterns('ex.views',
    url(r'^detail/(?P<pk>\d+)/$', 'detail', name='detail'),
)
