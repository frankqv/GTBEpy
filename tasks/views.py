from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def erro404(request):
    return render(request, 'frontend/erro404.html')

def erro500(request):
    return render(request, 'frontend/erro500.html')

def registrar(request):
    return render(request, 'frontend/registrar.html')

def escritorio(request):
    # Tu lógica aquí
    return render(request, 'frontend/escritorio.html')


def login(request):
    return render(request, 'frontend/login_view.html')
#Carpeta Admin
def admin_escritorio(request):
    return render(request, 'frontend/administrador/escritorio.html')



#Carpeta Categoria
def categoria_actualizar(request):
    return render(request, 'frontend/categoria/actualizar.html')

def categoria_eliminar(request):
    return render(request, 'frontend/categoria/eliminar.html')

def categoria_mostrar(request):
    return render(request, 'frontend/categoria/mostrar.html')

def categoria_nuevo(request):
    return render(request, 'frontend/categoria/nuevo.html')

#Carpeta Cliente
def cliente_escrtorio(request):
    return render(request, 'frontend/cliente/escritorio.html')

def cliente_plan(request):
    # Tu lógica aquí
    return render(request, 'frontend/cliente/plan.html')

def cliente_servicio(request):
    return render(request, 'frontend/cliente/servicio.html')

#Carpeta Clientes 
def clientes_actualizar(request):
    return render(request, 'frontend/clientes/actualizar.html')

def clientes_eliminar(request):
    return render(request, 'frontend/clientes/eliminar.html')

def clientes_importar(request):
    return render(request, 'frontend/clientes/importar.html')

def clientes_informacion(request):
    return render(request, 'frontend/clientes/informacion.html')

def clientes_mostrar(request):
    return render(request, 'frontend/clientes/mostrar.html')

def clientes_nuevo(request):
    return render(request, 'frontend/clientes/nuevo.html')

#Carpeta Compra
def compra_cancelar(request):
    return render(request, 'frontend/compra/cancelar.html')

def comprar_informacion(request):
    return render(request, 'frontend/compra/informacion.html')

def compra_mostrar(request):
    return render(request, 'frontend/compra/mostrar.html')

def compra_nuevo(request):
    return render(request, 'frontend/compra/nuevo.html')

def compra_ticket(request):
    return render(request, 'frontend/compra/ticket.html')

#Carpeta cuenta
def cuenta_configuracion(request):
    return render(request, 'frontend/cuenta/configuracion.html')

def cuenta_perfil(request):
    return render(request, 'frontend/cuenta/perfil.html')

def cuenta_perfil2(request):
    return render(request, 'frontend/cuenta/perfil2.html')

def cuenta_salir(request):
    return render(request, 'frontend/cuenta/salir.html')

#Carpeta Gastos
def gastos_mostrar(request):
    return render(request, 'frontend/gastos/mostrar.html')

def gastos_nuevo(request):
    return render(request, 'frontend/gastos/nuevo.html')

#Carpeta Graficos
def graficos_mostrar(request):
    return render(request, 'frontend/graficos/mostrar.html')

#Carpeta Plan
def plan_actualizar(request):
    return render(request, 'frontend/plan/actualizar.html')

def plan_eliminar(request):
    return render(request, 'frontend/plan/eliminar.html')

def plan_foto(request):
    return render(request, 'frontend/plan/foto.html')

def plan_informacion(request):
    return render(request, 'frontend/plan/informacion.html')

def plan_mostrar(request):
    return render(request, 'frontend/plan/mostrar.html')

def plan_nuevo(request):
    return render(request, 'frontend/plan/nuevo.html')

#Carpeta Producto
def producto_actualizar(request):
    return render(request, 'frontend/producto/actualizar.html')

def producto_eliminar(request):
    return render(request, 'frontend/producto/eliminar.html')

def producto_foto(request):
    return render(request, 'frontend/producto/foto.html')

def producto_informacion(request):
    return render(request, 'frontend/producto/informacion.html')

def producto_mostrar(request):
    return render(request, 'frontend/producto/mostrar.html')

def producto_nuevo(request):
    return render(request, 'frontend/producto/nuevo.html')

#Carpeta Reporte
def reporte_clientes(request):
    return render(request, 'frontend/reporte/clientes.html')

def reporte_filtro_producto(request):
    return render(request, 'frontend/reporte/filtro-producto.html')

def reporte_filtro_servicio(request):
    return render(request, 'frontend/reporte/filtro-servicio.html')

def reporte_productos(request):
    return render(request, 'frontend/reporte/productos.html')

def reporte_ventas(request):
    return render(request, 'frontend/ventas.html')

#Carpeta Servicio
def servicio_actualizar(request):
    return render(request, 'frontend/servicio/actualizar.html')

def servicio_correo(request):
    return render(request, 'frontend/servicio/correo.html')

def servicio_eliminar(request):
    return render(request, 'frontend/servicio/eliminar.html')

def servicio_mostrar(request):
    return render(request, 'frontend/servicio/mostrar.html')

def servicio_nuevo(request):
    return render(request, 'frontend/servicio/nuevo.html')

def servicio_ticket(request):
    return render(request, 'frontend/servicio/ticket.html')

def servicio_ver(request):
    return render(request, 'frontend/servicio/ver.html')

#Carpeta Usuario
def usuario_actualizar(request):
    return render(request, 'frontend/actualizar.html')

def usuario_eliminar(request):
    return render(request, 'frontend/usuario/eliminar.html')

def usuario_mostrar(request):
    return render(request, 'frontend/usuario/mostrar.html')

#Carpeta Venta
def venta_cancelar(request):
    return render(request, 'frontend/venta/cancelar.html')

def venta_eliminar(request):
    return render(request, 'frontend/venta/eliminar.html')

def venta_informacion(request):
    return render(request, 'frontend/venta/informacion.html')

def venta_mostrar(request):
    return render(request, 'frontend/venta/mostrar.html')

def venta_nuevo(request):
    return render(request, 'frontend/venta/nuevo.html')

def venta_ticket(request):
    return render(request, 'frontend/venta/ticket.html')