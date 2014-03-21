from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dropbox_test.views.home'),
    url(r'^cb$', 'dropbox_test.views.cb'),
    url(r'^file_list$', 'dropbox_test.views.file_list'),
    url(r'^login$', 'dropbox_test.views.login'),
    url(r'^signup$', 'dropbox_test.views.signup'),
    url(r'^admin/', include(admin.site.urls)),
)
