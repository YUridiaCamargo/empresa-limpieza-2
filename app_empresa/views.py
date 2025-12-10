from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    ClienteLimpieza, ServicioLimpieza, EmpleadoLimpieza, 
    ProgramacionServicio, FacturaLimpieza, MaterialLimpieza, UsoMaterial
)
from .forms import (
    ClienteLimpiezaForm, ServicioLimpiezaForm, EmpleadoLimpiezaForm, 
    ProgramacionServicioForm, FacturaLimpiezaForm, MaterialLimpiezaForm, UsoMaterialForm
)

def inicio(request):
    return render(request, 'inicio.html')

# Vistas para ClienteLimpieza
def ver_clientes(request):
    clientes = ClienteLimpieza.objects.all()
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteLimpiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteLimpiezaForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(ClienteLimpieza, pk=pk)
    if request.method == 'POST':
        form = ClienteLimpiezaForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteLimpiezaForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})

def borrar_cliente(request, pk):
    cliente = get_object_or_404(ClienteLimpieza, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})

# Vistas para ServicioLimpieza
def ver_servicios(request):
    servicios = ServicioLimpieza.objects.all()
    return render(request, 'servicios/ver_servicios.html', {'servicios': servicios})

def agregar_servicio(request):
    if request.method == 'POST':
        form = ServicioLimpiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_servicios')
    else:
        form = ServicioLimpiezaForm()
    return render(request, 'servicios/agregar_servicio.html', {'form': form})

def editar_servicio(request, pk):
    servicio = get_object_or_404(ServicioLimpieza, pk=pk)
    if request.method == 'POST':
        form = ServicioLimpiezaForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('ver_servicios')
    else:
        form = ServicioLimpiezaForm(instance=servicio)
    return render(request, 'servicios/editar_servicio.html', {'form': form})

def borrar_servicio(request, pk):
    servicio = get_object_or_404(ServicioLimpieza, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('ver_servicios')
    return render(request, 'servicios/borrar_servicio.html', {'servicio': servicio})

# Vistas para EmpleadoLimpieza
def ver_empleados(request):
    empleados = EmpleadoLimpieza.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoLimpiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoLimpiezaForm()
    return render(request, 'empleados/agregar_empleado.html', {'form': form})

def editar_empleado(request, pk):
    empleado = get_object_or_404(EmpleadoLimpieza, pk=pk)
    if request.method == 'POST':
        form = EmpleadoLimpiezaForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoLimpiezaForm(instance=empleado)
    return render(request, 'empleados/editar_empleado.html', {'form': form})

def borrar_empleado(request, pk):
    empleado = get_object_or_404(EmpleadoLimpieza, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})

# Vistas para ProgramacionServicio
def ver_programacion(request):
    programaciones = ProgramacionServicio.objects.all()
    return render(request, 'programacion/ver_programacion.html', {'programaciones': programaciones})

def agregar_programacion(request):
    if request.method == 'POST':
        form = ProgramacionServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_programacion')
    else:
        form = ProgramacionServicioForm()
    return render(request, 'programacion/agregar_programacion.html', {'form': form})

def editar_programacion(request, pk):
    programacion = get_object_or_404(ProgramacionServicio, pk=pk)
    if request.method == 'POST':
        form = ProgramacionServicioForm(request.POST, instance=programacion)
        if form.is_valid():
            form.save()
            return redirect('ver_programacion')
    else:
        form = ProgramacionServicioForm(instance=programacion)
    return render(request, 'programacion/editar_programacion.html', {'form': form})

def borrar_programacion(request, pk):
    programacion = get_object_or_404(ProgramacionServicio, pk=pk)
    if request.method == 'POST':
        programacion.delete()
        return redirect('ver_programacion')
    return render(request, 'programacion/borrar_programacion.html', {'programacion': programacion})

# Vistas para FacturaLimpieza
def ver_facturas(request):
    facturas = FacturaLimpieza.objects.all()
    return render(request, 'facturas/ver_facturas.html', {'facturas': facturas})

def agregar_factura(request):
    if request.method == 'POST':
        form = FacturaLimpiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_facturas')
    else:
        form = FacturaLimpiezaForm()
    return render(request, 'facturas/agregar_factura.html', {'form': form})

def editar_factura(request, pk):
    factura = get_object_or_404(FacturaLimpieza, pk=pk)
    if request.method == 'POST':
        form = FacturaLimpiezaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('ver_facturas')
    else:
        form = FacturaLimpiezaForm(instance=factura)
    return render(request, 'facturas/editar_factura.html', {'form': form})

def borrar_factura(request, pk):
    factura = get_object_or_404(FacturaLimpieza, pk=pk)
    if request.method == 'POST':
        factura.delete()
        return redirect('ver_facturas')
    return render(request, 'facturas/borrar_factura.html', {'factura': factura})

# Vistas para MaterialLimpieza
def ver_materiales(request):
    materiales = MaterialLimpieza.objects.all()
    return render(request, 'materiales/ver_materiales.html', {'materiales': materiales})

def agregar_material(request):
    if request.method == 'POST':
        form = MaterialLimpiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_materiales')
    else:
        form = MaterialLimpiezaForm()
    return render(request, 'materiales/agregar_material.html', {'form': form})

def editar_material(request, pk):
    material = get_object_or_404(MaterialLimpieza, pk=pk)
    if request.method == 'POST':
        form = MaterialLimpiezaForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('ver_materiales')
    else:
        form = MaterialLimpiezaForm(instance=material)
    return render(request, 'materiales/editar_material.html', {'form': form})

def borrar_material(request, pk):
    material = get_object_or_404(MaterialLimpieza, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('ver_materiales')
    return render(request, 'materiales/borrar_material.html', {'material': material})

# Vistas para UsoMaterial
def ver_usos(request):
    usos = UsoMaterial.objects.all()
    return render(request, 'usos/ver_usos.html', {'usos': usos})

def agregar_uso(request):
    if request.method == 'POST':
        form = UsoMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_usos')
    else:
        form = UsoMaterialForm()
    return render(request, 'usos/agregar_uso.html', {'form': form})

def editar_uso(request, pk):
    uso = get_object_or_404(UsoMaterial, pk=pk)
    if request.method == 'POST':
        form = UsoMaterialForm(request.POST, instance=uso)
        if form.is_valid():
            form.save()
            return redirect('ver_usos')
    else:
        form = UsoMaterialForm(instance=uso)
    return render(request, 'usos/editar_uso.html', {'form': form})

def borrar_uso(request, pk):
    uso = get_object_or_404(UsoMaterial, pk=pk)
    if request.method == 'POST':
        uso.delete()
        return redirect('ver_usos')
    return render(request, 'usos/borrar_uso.html', {'uso': uso})
