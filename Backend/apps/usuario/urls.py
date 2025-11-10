from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.usuario import views

urlpatterns = [
    # === RUTAS DE ROLES ===
    path('roles/', views.RolListView.as_view(), name='rol-list'),
    path('roles/<int:pk>/', views.RolDetailView.as_view(), name='rol-detail'),

    # === RUTAS DE AUTENTICACIÓN JWT ===
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # === RUTA DE REGISTRO DE USUARIOS ===
    path('registro/', views.RegistroUsuarioView.as_view(), name='usuario-registro'),

    # === RUTA DE CARACTERIZACIÓN DE APRENDICES ===
    path('caracterizacion/registrar/', views.CaracterizacionCreateView.as_view(), name='caracterizacion-create'),
]
