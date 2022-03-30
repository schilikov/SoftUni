from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Employees_App.employees.views import home, base, index

urlpatterns = [
                path('admin/', admin.site.urls),
                path('', home, name='home'),
                path('employee/', include('Employees_App.employees.urls')),
                path('basic/', base, name='basic'),
                path('index/', index, name='index'),
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
