"""
Definition of urls for tour.
"""

from django.conf.urls import include, url
import hellodjango.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', hellodjango.views.index, name='index'),
    url(r'^home$', hellodjango.views.index, name='home'),
    url(r'^about$', hellodjango.views.about, name='about'),
    # url(r'^tour/', include('tour.tour.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
