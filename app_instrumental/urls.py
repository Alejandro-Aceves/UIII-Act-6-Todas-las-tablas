from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Proveedores
    path('proveedores/', views.proveedores_list, name='proveedores_list'),
    path('proveedores/crear/', views.proveedor_create, name='proveedor_create'),
    path('proveedores/editar/<int:pk>/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedores/eliminar/<int:pk>/', views.proveedor_delete, name='proveedor_delete'),
    
    # Clientes
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    
    # Instrumentos
    path('instrumentos/', views.instrumentos_list, name='instrumentos_list'),
    path('instrumentos/crear/', views.instrumento_create, name='instrumento_create'),
    path('instrumentos/editar/<int:pk>/', views.instrumento_edit, name='instrumento_edit'),
    path('instrumentos/eliminar/<int:pk>/', views.instrumento_delete, name='instrumento_delete'),
    
    # Empleados
    path('empleados/', views.empleados_list, name='empleados_list'),
    path('empleados/crear/', views.empleado_create, name='empleado_create'),
    path('empleados/editar/<int:pk>/', views.empleado_edit, name='empleado_edit'),
    path('empleados/eliminar/<int:pk>/', views.empleado_delete, name='empleado_delete'),
    
    # Inventarios
    path('inventarios/', views.inventarios_list, name='inventarios_list'),
    path('inventarios/crear/', views.inventario_create, name='inventario_create'),
    path('inventarios/editar/<int:pk>/', views.inventario_edit, name='inventario_edit'),
    path('inventarios/eliminar/<int:pk>/', views.inventario_delete, name='inventario_delete'),
    
    # Ventas
    path('ventas/', views.ventas_list, name='ventas_list'),
    path('ventas/crear/', views.venta_create, name='venta_create'),
    path('ventas/editar/<int:pk>/', views.venta_edit, name='venta_edit'),
    path('ventas/eliminar/<int:pk>/', views.venta_delete, name='venta_delete'),
    
    # Detalles de Venta
    path('detalles-venta/', views.detalles_venta_list, name='detalles_venta_list'),
    path('detalles-venta/crear/', views.detalle_venta_create, name='detalle_venta_create'),
    path('detalles-venta/editar/<int:pk>/', views.detalle_venta_edit, name='detalle_venta_edit'),
    path('detalles-venta/eliminar/<int:pk>/', views.detalle_venta_delete, name='detalle_venta_delete'),
]