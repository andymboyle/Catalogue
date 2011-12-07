from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^catalogue/$', 'catalogue.app.views.index'),
    (r'^catalogue/book/(?P<un_id>[-\w]+)/(?P<title>[-\w]+)/$', 'catalogue.app.views.book'),
    (r'^catalogue/movie/(?P<un_id>[-\w]+)/(?P<title>[-\w]+)/$', 'catalogue.app.views.movie'),
    (r'^catalogue/currently-reading/$', 'catalogue.app.views.currently_reading'),
    (r'^catalogue/admin/', include(admin.site.urls)),
)