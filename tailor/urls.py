from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('customer/', include('customer.urls')),
                  path('measurement/', include('measurement.urls')),
                  path('order/', include('order.urls')),
                  path('', include('dashbord.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
