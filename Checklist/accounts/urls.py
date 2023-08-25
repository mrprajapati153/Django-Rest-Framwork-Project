
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts import views

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/register/',views.RegisterAPIView.as_view(),name='register'),
    path('api/logout/',views.LogoutAPIView.as_view(),name='logout')
    
]