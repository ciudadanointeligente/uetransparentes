from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("", include("leyes.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
