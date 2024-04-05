
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),  # Actualiza la ruta para la vista home
    #frontend
    path('frontend/erro404',views.erro404),
    path('frontend/erro500', views.erro500),
    path('frontend/login.html', views.login),
]
