from django.contrib import admin
from django.urls import path

from block.views import invitation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invite/<str:token>/', invitation_view, name='invitation_view'),
]

