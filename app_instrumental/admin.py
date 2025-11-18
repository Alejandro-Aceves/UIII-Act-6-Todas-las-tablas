from django.contrib import admin
from .models import Proveedor, Cliente, Instrumento, Empleado, Inventario, Venta, DetalleVenta


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_empresa', 'telefono', 'email', 'rfc', 'ciudad', 'activo')
    search_fields = ('nombre_empresa', 'email', 'telefono', 'rfc')
    list_filter = ('activo', 'ciudad')
    ordering = ('nombre_empresa',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono', 'ciudad', 'rfc', 'activo')
    search_fields = ('nombre', 'email', 'telefono', 'ciudad', 'rfc')
    list_filter = ('ciudad', 'activo')
    ordering = ('nombre',)


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('id_instrumento', 'nombre', 'marca', 'modelo', 'categoria', 'precio_compra', 'precio_venta', 'id_proveedor')
    search_fields = ('nombre', 'marca', 'modelo')
    list_filter = ('marca', 'categoria', 'id_proveedor')
    ordering = ('nombre',)
    raw_id_fields = ('id_proveedor',)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('id_proveedor')
        return queryset


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'puesto', 'salario', 'edad', 'telefono', 'activo')
    search_fields = ('nombre', 'puesto', 'nss', 'telefono')
    list_filter = ('puesto', 'activo')
    ordering = ('nombre',)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'id_instrumento', 'num_bodega', 'cantidad_actual', 'cantidad_minima', 'costo_unitario', 'id_empleado')
    search_fields = ('num_bodega',)
    list_filter = ('num_bodega', 'ultima_actualizacion')
    ordering = ('-ultima_actualizacion',)
    readonly_fields = ('ultima_actualizacion',)
    raw_id_fields = ('id_empleado', 'id_instrumento')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('id_empleado', 'id_instrumento')
        return queryset


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'fecha_venta', 'id_empleado', 'id_cliente', 'subtotal', 'total', 'estado')
    search_fields = ('id_venta',)
    list_filter = ('estado', 'fecha_venta', 'id_empleado', 'id_cliente')
    ordering = ('-fecha_venta',)
    readonly_fields = ('fecha_venta',)
    raw_id_fields = ('id_empleado', 'id_cliente')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('id_empleado', 'id_cliente')
        return queryset


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_venta', 'id_venta', 'id_instrumento', 'cantidad', 'precio_unitario', 'descuento_linea', 'subtotal')
    search_fields = ('id_detalle_venta',)
    list_filter = ('id_venta', 'id_instrumento')
    ordering = ('-id_detalle_venta',)
    raw_id_fields = ('id_venta', 'id_instrumento')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('id_venta', 'id_instrumento')
        return queryset