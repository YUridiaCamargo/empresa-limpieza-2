from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # URLs para ClienteLimpieza
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    # URLs para ServicioLimpieza
    path('servicios/', views.ver_servicios, name='ver_servicios'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/editar/<int:pk>/', views.editar_servicio, name='editar_servicio'),
    path('servicios/borrar/<int:pk>/', views.borrar_servicio, name='borrar_servicio'),

    # URLs para EmpleadoLimpieza
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),

    # URLs para ProgramacionServicio
    path('programacion/', views.ver_programacion, name='ver_programacion'),
    path('programacion/agregar/', views.agregar_programacion, name='agregar_programacion'),
    path('programacion/editar/<int:pk>/', views.editar_programacion, name='editar_programacion'),
    path('programacion/borrar/<int:pk>/', views.borrar_programacion, name='borrar_programacion'),

    # URLs para FacturaLimpieza
    path('facturas/', views.ver_facturas, name='ver_facturas'),
    path('facturas/agregar/', views.agregar_factura, name='agregar_factura'),
    path('facturas/editar/<int:pk>/', views.editar_factura, name='editar_factura'),
    path('facturas/borrar/<int:pk>/', views.borrar_factura, name='borrar_factura'),

    # URLs para MaterialLimpieza
    path('materiales/', views.ver_materiales, name='ver_materiales'),
    path('materiales/agregar/', views.agregar_material, name='agregar_material'),
    path('materiales/editar/<int:pk>/', views.editar_material, name='editar_material'),
    path('materiales/borrar/<int:pk>/', views.borrar_material, name='borrar_material'),

    # URLs para UsoMaterial
    path('usos/', views.ver_usos, name='ver_usos'),
    path('usos/agregar/', views.agregar_uso, name='agregar_uso'),
    path('usos/editar/<int:pk>/', views.editar_uso, name='editar_uso'),
    path('usos/borrar/<int:pk>/', views.borrar_uso, name='borrar_uso'),
]
