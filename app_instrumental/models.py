from django.db import models

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=200, verbose_name="Nombre de Empresa")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    rfc = models.CharField(max_length=100, verbose_name="RFC")
    direccion = models.TextField(blank=True, verbose_name="Dirección")
    ciudad = models.CharField(max_length=100, blank=True, verbose_name="Ciudad")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    def __str__(self):
        return self.nombre_empresa
    
    class Meta:
        verbose_name_plural = "Proveedores"


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    email = models.EmailField(max_length=100, verbose_name="Email")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    direccion = models.CharField(max_length=300, verbose_name="Dirección")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    rfc = models.CharField(max_length=100, blank=True, verbose_name="RFC")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Clientes"


class Instrumento(models.Model):
    CATEGORIAS = [
        ('CUERDA', 'Cuerda'),
        ('VIENTO', 'Viento'),
        ('PERCUSION', 'Percusión'),
        ('TECLADO', 'Teclado'),
        ('ELECTRONICO', 'Electrónico'),
        ('OTRO', 'Otro'),
    ]
    
    id_instrumento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    marca = models.CharField(max_length=100, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OTRO', verbose_name="Categoría")
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Compra")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Venta")
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, related_name='instrumentos', verbose_name="Proveedor")
    
    def __str__(self):
        return f"{self.nombre} - {self.marca}"
    
    class Meta:
        verbose_name_plural = "Instrumentos"


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    puesto = models.CharField(max_length=100, verbose_name="Puesto")
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario")
    nss = models.CharField(max_length=50, verbose_name="NSS")
    edad = models.IntegerField(verbose_name="Edad")
    telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    def __str__(self):
        return f"{self.nombre} - {self.puesto}"
    
    class Meta:
        verbose_name_plural = "Empleados"


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    id_instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, related_name='inventarios', verbose_name="Instrumento")
    id_empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='inventarios', verbose_name="Empleado Responsable")
    num_bodega = models.CharField(max_length=50, verbose_name="Número de Bodega")
    cantidad_actual = models.IntegerField(verbose_name="Cantidad Actual")
    cantidad_minima = models.IntegerField(default=5, verbose_name="Cantidad Mínima")
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Unitario")
    ultima_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    
    def __str__(self):
        return f"{self.id_instrumento.nombre} - Bodega {self.num_bodega}"
    
    def requiere_reorden(self):
        return self.cantidad_actual <= self.cantidad_minima
    
    class Meta:
        verbose_name_plural = "Inventarios"


class Venta(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADA', 'Pagada'),
        ('CANCELADA', 'Cancelada'),
        ('ENTREGADA', 'Entregada'),
    ]
    
    id_venta = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas', verbose_name="Empleado")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas', verbose_name="Cliente")
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Venta")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Descuento")
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Impuesto")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE', verbose_name="Estado")
    
    def __str__(self):
        return f"Venta #{self.id_venta} - Total: ${self.total}"
    
    def calcular_total(self):
        return self.subtotal - self.descuento + self.impuesto
    
    class Meta:
        verbose_name_plural = "Ventas"


class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles', verbose_name="Venta")
    id_instrumento = models.ForeignKey(Instrumento, on_delete=models.SET_NULL, null=True, related_name='detalles_venta', verbose_name="Instrumento")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    descuento_linea = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Descuento")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    notas = models.TextField(blank=True, verbose_name="Notas")
    
    def __str__(self):
        return f"Detalle Venta #{self.id_detalle_venta}"
    
    def calcular_subtotal(self):
        return (self.precio_unitario * self.cantidad) - self.descuento_linea
    
    class Meta:
        verbose_name_plural = "Detalles de Venta"