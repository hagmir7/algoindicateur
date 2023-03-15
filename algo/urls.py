
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django_summernote import urls as summernote_urls

urlpatterns = [
     path('i18n/', include('django.conf.urls.i18n')),

]


urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('', include('users.urls')),
    path('summernote/', include('django_summernote.urls')),
    

)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)