from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from notas import views as notas_views  # Corrigido: importar views do app 'notas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notas/', include('notas.urls')),  # Certifique-se de que o arquivo 'notas/urls.py' existe e está correto
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', notas_views.register, name='register'),  # Certifique-se de que a view 'register' existe no app 'notas'
    path('', notas_views.lista_notas, name='home'),  # Certifique-se de que a view 'lista_notas' existe no app 'notas'
]
