from django.contrib import admin
from django.urls import path, include
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
    path('frontend/administrador/escritorio.html', views.admin_escritorio),
    # Carpeta Cliente
    path('frontend/cliente/escritorio/', views.cliente_escrtorio, name='cliente_escritorio'),
    path('frontend/cliente/plan', views.cliente_plan),
    path('frontend/cliente/servicio', views.cliente_servicio),
    # Carpeta Categoria
    path('frontend/categoria/actualizar', views.categoria_actualizar),
    path('frontend/categoria/eliminar', views.categoria_eliminar),
    path('frontend/categoria/mostrar', views.categoria_mostrar),
    path('frontend/categoria/nuevo', views.categoria_nuevo),
    # Carpeta Clientes
    path('frontend/clientes/actualizar', views.clientes_actualizar),
    path('frontend/clientes/eliminar', views.clientes_eliminar),
    path('frontend/clientes/importar', views.clientes_importar),
    path('frontend/clientes/informacion', views.clientes_informacion),
    path('frontend/clientes/mostrar', views.clientes_mostrar),
    path('frontend/clientes/nuevo', views.clientes_nuevo),
    # Carpeta Compra
    path('frontend/compra/cancelar', views.compra_cancelar),
    path('frontend/compra/informacion', views.comprar_informacion),
    path('frontend/compra/mostrar', views.compra_mostrar),
    path('frontend/compra/nuevo', views.compra_nuevo),
    path('frontend/compra/ticket', views.compra_ticket),
    # Carpeta Cuenta
    path('frontend/cuenta/configuracion', views.cuenta_configuracion),
    path('frontend/cuenta/perfil', views.cuenta_perfil),
    path('frontend/cuenta/perfil2', views.cuenta_perfil2),
    path('frontend/cuenta/salir', views.cuenta_salir),
    # Carpeta Gastos
    path('frontend/gastos/mostrar', views.gastos_mostrar),
    path('frontend/gastos/nuevo', views.gastos_nuevo),
    # Carpeta Graficos
    path('frontend/graficos/mostrar', views.graficos_mostrar),
    # Carpeta Plan
    path('frontend/plan/actualizar', views.plan_actualizar),
    path('frontend/plan/eliminar', views.plan_eliminar),
    path('frontend/plan/foto', views.plan_foto),
    path('frontend/plan/informacion', views.plan_informacion),
    path('frontend/plan/mostrar', views.plan_mostrar),
    path('frontend/plan/nuevo', views.plan_nuevo),
    # Carpeta Producto
    path('frontend/producto/actualizar', views.producto_actualizar),
    path('frontend/producto/eliminar', views.producto_eliminar),
    path('frontend/producto/foto', views.producto_foto),
    path('frontend/producto/informacion', views.producto_informacion),
    path('frontend/producto/mostrar', views.producto_mostrar),
    path('frontend/producto/nuevo', views.producto_nuevo),
    # Carpeta Reporte
    path('frontend/reporte/clientes', views.reporte_clientes),
    path('frontend/reporte/filtro-producto', views.reporte_filtro_producto),
    path('frontend/reporte/filtro-servicio', views.reporte_filtro_servicio),
    path('frontend/reporte/productos', views.reporte_productos),
    path('frontend/ventas', views.reporte_ventas),
    # Carpeta Servicio
    path('frontend/servicio/actualizar', views.servicio_actualizar),
    path('frontend/servicio/correo', views.servicio_correo),
    path('frontend/servicio/eliminar', views.servicio_eliminar),
    path('frontend/servicio/mostrar', views.servicio_mostrar),
    path('frontend/servicio/nuevo', views.servicio_nuevo),
    path('frontend/servicio/ticket', views.servicio_ticket),
    path('frontend/servicio/ver', views.servicio_ver),
    # Carpeta Usuario
    path('frontend/usuario/actualizar', views.usuario_actualizar),
    path('frontend/usuario/eliminar', views.usuario_eliminar),
    path('frontend/usuario/mostrar', views.usuario_mostrar),
    # Carpeta Venta
    path('frontend/venta/cancelar', views.venta_cancelar),
    path('frontend/venta/eliminar', views.venta_eliminar),
    path('frontend/venta/informacion', views.venta_informacion),
    path('frontend/venta/mostrar', views.venta_mostrar),
    path('frontend/venta/nuevo', views.venta_nuevo),
    path('frontend/venta/ticket', views.venta_ticket),
    # Agrega aquí el resto de las URLs que faltan...
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
