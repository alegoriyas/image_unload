"""
Definition of urls for image_unload.
"""

from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls', namespace='core')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)