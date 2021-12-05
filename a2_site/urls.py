from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path(r'edilton/', include('edilton.urls')),
   # path(r'caio/', include('caio.urls')),
    path(r'dani/', include('dani.urls')),
   # path(r'pedro/', include('pedro.urls')),
    path('', RedirectView.as_view(url='/website/', permanent=False)),
    *staticfiles_urlpatterns()
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
