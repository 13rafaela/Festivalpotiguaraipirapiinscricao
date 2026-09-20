from django.contrib import admin
from django.urls import path
from festival_app.views import cadastro

urlpatterns = [
    path("", cadastro, name="home"),
    path("cadastro/", cadastro, name="cadastro"),
    path("admin/", admin.site.urls),
]