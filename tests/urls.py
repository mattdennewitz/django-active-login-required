from django.conf.urls import patterns, url


urlpatterns = patterns(
    'tests.views',

    url(r'^test_view_a/$', 'test_view_a'),
)
