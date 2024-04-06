from django.contrib import admin
from django.urls import path,  include
from django.conf import settings
from django.conf.urls.static import static
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),  
    path('home.html', views.home),


    path('frontend/escritorio', views.escritorio, name='escritorio'),
    path('frontend/erro404', views.erro404),
    path('frontend/erro500', views.erro500),
    path('frontend/login_view.html', views.login),
    path('frontend/registrar.html', views.registrar),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
