from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-core/', include('core.urls')),
    url(r'^api-hotel/', include('hotel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
