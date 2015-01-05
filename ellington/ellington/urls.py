from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ellington.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ek_site.views.index', name='index'),
    url(r'^about/', 'ek_site.views.about', name = 'about'),
    url(r'^projects/', 'ek_site.views.projects', name='projects'),
    url(r'^contact/', 'ek_site.views.contact', name='contact'),
    url(r'^thanks/', 'ek_site.views.thanks', name='thanks')
)
urlpatterns += staticfiles_urlpatterns()
