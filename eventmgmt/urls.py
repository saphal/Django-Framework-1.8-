from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'eventmgmt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^about/$', 'eventmgmt.views.about', name='about'),
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.url')),
    url(r'^accounts/', include('registration.backends.default.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)