from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('jeopardly/', include('jeopardly.urls')),
    path('admin/', admin.site.urls),
]