# my_prj/urls.py

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_app/', include('admin_app.urls')),  # admin_app URL을 포함
]
