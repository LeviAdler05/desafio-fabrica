from django.urls import path, redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notas/', include('notas.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', notas_views.register, name='register'),
    path('accounts/login/', lambda request: redirect('/login/')),  # Redireciona para a URL correta
    path('', lambda request: redirect('lista_notas'), name='home'),
]
