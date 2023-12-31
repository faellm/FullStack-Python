from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls')),
    path("", include('loja.urls')),
    path('/login', include('login.urls')),

]
