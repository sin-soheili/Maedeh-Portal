from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('ticketing/', include('ticketing.urls')),
    path('associations/', include('associations.urls')),
    path('contact/', include('contact.urls')),
    path('announcements/', include('announcements.urls')),
    path('', include('pages.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
