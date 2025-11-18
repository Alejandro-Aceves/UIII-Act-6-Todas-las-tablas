from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proveedor, Cliente, Instrumento, Empleado, Inventario, Venta, DetalleVenta

def home(request):
    """Vista de inicio"""
    return render(request, 'app_instrumental/home.html')

# ========== PROVEEDORES ==========
def proveedores_list(request):
    query = request.GET.get('q', '')
    if query:
        proveedores = Proveedor.objects.filter(
            nombre_empresa__icontains=query
        ) | Proveedor.objects.filter(
            email__icontains=query
        ) | Proveedor.objects.filter(
            telefono__icontains=query
        )
    else:
        proveedores = Proveedor.objects.all()
    return render(request, 'app_instrumental/proveedores_list.html', {
        'proveedores': proveedores,
        'query': query
    })

def proveedor_create(request):
    if request.method == 'POST':
        proveedor = Proveedor(
            nombre_empresa=request.POST['nombre_empresa'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            rfc=request.POST['rfc'],
            direccion=request.POST.get('direccion', ''),
            ciudad=request.POST.get('ciudad', ''),
            activo=request.POST.get('activo', 'on') == 'on'
        )
        proveedor.save()
        messages.success(request, 'Proveedor creado exitosamente')
        return redirect('proveedores_list')
    return render(request, 'app_instrumental/proveedor_form.html')

def proveedor_edit(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre_empresa = request.POST['nombre_empresa']
        proveedor.telefono = request.POST['telefono']
        proveedor.email = request.POST['email']
        proveedor.rfc = request.POST['rfc']
        proveedor.direccion = request.POST.get('direccion', '')
        proveedor.ciudad = request.POST.get('ciudad', '')
        proveedor.activo = request.POST.get('activo', 'off') == 'on'
        proveedor.save()
        messages.success(request, 'Proveedor actualizado exitosamente')
        return redirect('proveedores_list')
    return render(request, 'app_instrumental/proveedor_form.html', {'proveedor': proveedor})

def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado exitosamente')
    return redirect('proveedores_list')

# ========== CLIENTES ==========
def clientes_list(request):
    query = request.GET.get('q', '')
    if query:
        clientes = Cliente.objects.filter(
            nombre__icontains=query
        ) | Cliente.objects.filter(
            email__icontains=query
        ) | Cliente.objects.filter(
            ciudad__icontains=query
        ) | Cliente.objects.filter(
            telefono__icontains=query
        )
    else:
        clientes = Cliente.objects.all()
    return render(request, 'app_instrumental/clientes_list.html', {
        'clientes': clientes,
        'query': query
    })

def cliente_create(request):
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.POST['nombre'],
            email=request.POST['email'],
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion'],
            ciudad=request.POST['ciudad'],
            rfc=request.POST.get('rfc', ''),
            activo=request.POST.get('activo', 'on') == 'on'
        )
        cliente.save()
        messages.success(request, 'Cliente creado exitosamente')
        return redirect('clientes_list')
    return render(request, 'app_instrumental/cliente_form.html')

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.email = request.POST['email']
        cliente.telefono = request.POST['telefono']
        cliente.direccion = request.POST['direccion']
        cliente.ciudad = request.POST['ciudad']
        cliente.rfc = request.POST.get('rfc', '')
        cliente.activo = request.POST.get('activo', 'off') == 'on'
        cliente.save()
        messages.success(request, 'Cliente actualizado exitosamente')
        return redirect('clientes_list')
    return render(request, 'app_instrumental/cliente_form.html', {'cliente': cliente})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('clientes_list')

# ========== INSTRUMENTOS ==========
def instrumentos_list(request):
    query = request.GET.get('q', '')
    if query:
        instrumentos = Instrumento.objects.filter(
            nombre__icontains=query
        ) | Instrumento.objects.filter(
            marca__icontains=query
        ) | Instrumento.objects.filter(
            modelo__icontains=query
        )
    else:
        instrumentos = Instrumento.objects.all()
    return render(request, 'app_instrumental/instrumentos_list.html', {
        'instrumentos': instrumentos,
        'query': query
    })

def instrumento_create(request):
    if request.method == 'POST':
        instrumento = Instrumento(
            nombre=request.POST['nombre'],
            marca=request.POST['marca'],
            modelo=request.POST['modelo'],
            categoria=request.POST['categoria'],
            precio_compra=request.POST['precio_compra'],
            precio_venta=request.POST['precio_venta'],
            id_proveedor_id=request.POST.get('id_proveedor') or None
        )
        instrumento.save()
        messages.success(request, 'Instrumento creado exitosamente')
        return redirect('instrumentos_list')
    proveedores = Proveedor.objects.all()
    categorias = Instrumento.CATEGORIAS
    return render(request, 'app_instrumental/instrumento_form.html', {
        'proveedores': proveedores,
        'categorias': categorias
    })

def instrumento_edit(request, pk):
    instrumento = get_object_or_404(Instrumento, pk=pk)
    if request.method == 'POST':
        instrumento.nombre = request.POST['nombre']
        instrumento.marca = request.POST['marca']
        instrumento.modelo = request.POST['modelo']
        instrumento.categoria = request.POST['categoria']
        instrumento.precio_compra = request.POST['precio_compra']
        instrumento.precio_venta = request.POST['precio_venta']
        instrumento.id_proveedor_id = request.POST.get('id_proveedor') or None
        instrumento.save()
        messages.success(request, 'Instrumento actualizado exitosamente')
        return redirect('instrumentos_list')
    proveedores = Proveedor.objects.all()
    categorias = Instrumento.CATEGORIAS
    return render(request, 'app_instrumental/instrumento_form.html', {
        'instrumento': instrumento,
        'proveedores': proveedores,
        'categorias': categorias
    })

def instrumento_delete(request, pk):
    instrumento = get_object_or_404(Instrumento, pk=pk)
    instrumento.delete()
    messages.success(request, 'Instrumento eliminado exitosamente')
    return redirect('instrumentos_list')

# ========== EMPLEADOS ==========
def empleados_list(request):
    query = request.GET.get('q', '')
    if query:
        empleados = Empleado.objects.filter(
            nombre__icontains=query
        ) | Empleado.objects.filter(
            puesto__icontains=query
        ) | Empleado.objects.filter(
            nss__icontains=query
        )
    else:
        empleados = Empleado.objects.all()
    return render(request, 'app_instrumental/empleados_list.html', {
        'empleados': empleados,
        'query': query
    })

def empleado_create(request):
    if request.method == 'POST':
        empleado = Empleado(
            nombre=request.POST['nombre'],
            puesto=request.POST['puesto'],
            salario=request.POST['salario'],
            nss=request.POST['nss'],
            edad=request.POST['edad'],
            telefono=request.POST.get('telefono', ''),
            activo=request.POST.get('activo', 'on') == 'on'
        )
        empleado.save()
        messages.success(request, 'Empleado creado exitosamente')
        return redirect('empleados_list')
    return render(request, 'app_instrumental/empleado_form.html')

def empleado_edit(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.puesto = request.POST['puesto']
        empleado.salario = request.POST['salario']
        empleado.nss = request.POST['nss']
        empleado.edad = request.POST['edad']
        empleado.telefono = request.POST.get('telefono', '')
        empleado.activo = request.POST.get('activo', 'off') == 'on'
        empleado.save()
        messages.success(request, 'Empleado actualizado exitosamente')
        return redirect('empleados_list')
    return render(request, 'app_instrumental/empleado_form.html', {'empleado': empleado})

def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.delete()
    messages.success(request, 'Empleado eliminado exitosamente')
    return redirect('empleados_list')

# ========== INVENTARIOS ==========
def inventarios_list(request):
    query = request.GET.get('q', '')
    if query:
        inventarios = Inventario.objects.filter(
            num_bodega__icontains=query
        )
    else:
        inventarios = Inventario.objects.all()
    return render(request, 'app_instrumental/inventarios_list.html', {
        'inventarios': inventarios,
        'query': query
    })

def inventario_create(request):
    if request.method == 'POST':
        inventario = Inventario(
            id_instrumento_id=request.POST['id_instrumento'],
            id_empleado_id=request.POST.get('id_empleado') or None,
            num_bodega=request.POST['num_bodega'],
            cantidad_actual=request.POST['cantidad_actual'],
            cantidad_minima=request.POST.get('cantidad_minima', 5),
            costo_unitario=request.POST['costo_unitario']
        )
        inventario.save()
        messages.success(request, 'Inventario creado exitosamente')
        return redirect('inventarios_list')
    empleados = Empleado.objects.all()
    instrumentos = Instrumento.objects.all()
    return render(request, 'app_instrumental/inventario_form.html', {
        'empleados': empleados,
        'instrumentos': instrumentos
    })

def inventario_edit(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        inventario.id_instrumento_id = request.POST['id_instrumento']
        inventario.id_empleado_id = request.POST.get('id_empleado') or None
        inventario.num_bodega = request.POST['num_bodega']
        inventario.cantidad_actual = request.POST['cantidad_actual']
        inventario.cantidad_minima = request.POST.get('cantidad_minima', 5)
        inventario.costo_unitario = request.POST['costo_unitario']
        inventario.save()
        messages.success(request, 'Inventario actualizado exitosamente')
        return redirect('inventarios_list')
    empleados = Empleado.objects.all()
    instrumentos = Instrumento.objects.all()
    return render(request, 'app_instrumental/inventario_form.html', {
        'inventario': inventario,
        'empleados': empleados,
        'instrumentos': instrumentos
    })

def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    inventario.delete()
    messages.success(request, 'Inventario eliminado exitosamente')
    return redirect('inventarios_list')

# ========== VENTAS ==========
def ventas_list(request):
    query = request.GET.get('q', '')
    ventas = Venta.objects.all()
    if query:
        # Intentar buscar por ID de venta
        try:
            venta_id = int(query)
            ventas = ventas.filter(id_venta=venta_id)
        except ValueError:
            # Si no es un número, buscar por nombres de cliente o empleado
            ventas = ventas.filter(
                id_cliente__nombre__icontains=query
            ) | ventas.filter(
                id_empleado__nombre__icontains=query
            )
    return render(request, 'app_instrumental/ventas_list.html', {
        'ventas': ventas,
        'query': query
    })

def venta_create(request):
    if request.method == 'POST':
        venta = Venta(
            id_empleado_id=request.POST.get('id_empleado') or None,
            id_cliente_id=request.POST.get('id_cliente') or None,
            subtotal=request.POST['subtotal'],
            descuento=request.POST.get('descuento', 0),
            impuesto=request.POST.get('impuesto', 0),
            total=request.POST['total'],
            estado=request.POST.get('estado', 'PENDIENTE')
        )
        venta.save()
        messages.success(request, 'Venta creada exitosamente')
        return redirect('ventas_list')
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    estados = Venta.ESTADOS
    return render(request, 'app_instrumental/venta_form.html', {
        'empleados': empleados,
        'clientes': clientes,
        'estados': estados
    })

def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.id_empleado_id = request.POST.get('id_empleado') or None
        venta.id_cliente_id = request.POST.get('id_cliente') or None
        venta.subtotal = request.POST['subtotal']
        venta.descuento = request.POST.get('descuento', 0)
        venta.impuesto = request.POST.get('impuesto', 0)
        venta.total = request.POST['total']
        venta.estado = request.POST.get('estado', 'PENDIENTE')
        venta.save()
        messages.success(request, 'Venta actualizada exitosamente')
        return redirect('ventas_list')
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    estados = Venta.ESTADOS
    return render(request, 'app_instrumental/venta_form.html', {
        'venta': venta,
        'empleados': empleados,
        'clientes': clientes,
        'estados': estados
    })

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    venta.delete()
    messages.success(request, 'Venta eliminada exitosamente')
    return redirect('ventas_list')

# ========== DETALLES DE VENTA ==========
def detalles_venta_list(request):
    query = request.GET.get('q', '')
    detalles = DetalleVenta.objects.all()
    if query:
        # Intentar buscar por ID
        try:
            detalle_id = int(query)
            detalles = detalles.filter(id_detalle_venta=detalle_id)
        except ValueError:
            # Buscar por nombre de instrumento
            detalles = detalles.filter(
                id_instrumento__nombre__icontains=query
            ) | detalles.filter(
                id_instrumento__marca__icontains=query
            )
    return render(request, 'app_instrumental/detalles_venta_list.html', {
        'detalles': detalles,
        'query': query
    })

def detalle_venta_create(request):
    if request.method == 'POST':
        detalle = DetalleVenta(
            id_venta_id=request.POST['id_venta'],
            id_instrumento_id=request.POST['id_instrumento'],
            cantidad=request.POST['cantidad'],
            precio_unitario=request.POST['precio_unitario'],
            descuento_linea=request.POST.get('descuento_linea', 0),
            subtotal=request.POST['subtotal'],
            notas=request.POST.get('notas', '')
        )
        detalle.save()
        messages.success(request, 'Detalle de venta creado exitosamente')
        return redirect('detalles_venta_list')
    ventas = Venta.objects.all()
    instrumentos = Instrumento.objects.all()
    return render(request, 'app_instrumental/detalle_venta_form.html', {
        'ventas': ventas,
        'instrumentos': instrumentos
    })

def detalle_venta_edit(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == 'POST':
        detalle.id_venta_id = request.POST['id_venta']
        detalle.id_instrumento_id = request.POST['id_instrumento']
        detalle.cantidad = request.POST['cantidad']
        detalle.precio_unitario = request.POST['precio_unitario']
        detalle.descuento_linea = request.POST.get('descuento_linea', 0)
        detalle.subtotal = request.POST['subtotal']
        detalle.notas = request.POST.get('notas', '')
        detalle.save()
        messages.success(request, 'Detalle de venta actualizado exitosamente')
        return redirect('detalles_venta_list')
    ventas = Venta.objects.all()
    instrumentos = Instrumento.objects.all()
    return render(request, 'app_instrumental/detalle_venta_form.html', {
        'detalle': detalle,
        'ventas': ventas,
        'instrumentos': instrumentos
    })

def detalle_venta_delete(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    detalle.delete()
    messages.success(request, 'Detalle de venta eliminado exitosamente')
    return redirect('detalles_venta_list')