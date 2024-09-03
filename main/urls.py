from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from block.views import invitation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invite/<str:token>/', invitation_view, name='invitation_view'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
