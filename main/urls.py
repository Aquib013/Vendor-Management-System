from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from main.index_view import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("views-auth/", include("rest_framework.urls")),
    path("get-token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh-token", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify-token", TokenVerifyView.as_view(), name="token_verify"),
    path("", home, name="home"),
    path("api/v1/", include("svc.urls")),
]
