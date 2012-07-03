from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'', TemplateView.as_view(template_name="base.html")),
)
