from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('сourses/', include('courses.urls')),
    path('profile/', include('users.urls')),
    path('accounts/', include("allauth.urls")),
    path('faqs/', include('faqs.urls')),
    path('petitions/', include('petitions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
