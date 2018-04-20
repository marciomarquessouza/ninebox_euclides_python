# ninebox/urls.py

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('global_data/', include('global_data.urls')),
    path('admin/', admin.site.urls),
]
