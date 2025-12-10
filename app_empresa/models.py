from django.db import models

class ClienteLimpieza(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    contacto_principal = models.CharField(max_length=100)
    email_contacto = models.EmailField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    direccion_servicio = models.CharField(max_length=255)
    tipo_negocio = models.CharField(max_length=100)
    fecha_inicio_contrato = models.DateField()
    estado_contrato = models.CharField(max_length=50)
    frecuencia_servicio = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_empresa

class ServicioLimpieza(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo_estandar = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_estimada_horas = models.IntegerField()
    productos_usados = models.TextField()
    requiere_equipo_especial = models.BooleanField(default=False)
    categoria_servicio = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_servicio

class EmpleadoLimpieza(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario_hora = models.DecimalField(max_digits=5, decimal_places=2)
    turno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    certificaciones_seguridad = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ProgramacionServicio(models.Model):
    id_cliente = models.ForeignKey(ClienteLimpieza, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(ServicioLimpieza, on_delete=models.CASCADE)
    fecha_programada = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado_servicio = models.CharField(max_length=50)
    observaciones_cliente = models.TextField()
    id_empleado_asignado = models.ForeignKey(EmpleadoLimpieza, on_delete=models.CASCADE)

    def __str__(self):
        return f"Servicio a {self.id_cliente.nombre_empresa} el {self.fecha_programada}"

class FacturaLimpieza(models.Model):
    id_cliente = models.ForeignKey(ClienteLimpieza, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    id_programacion_asociada = models.ForeignKey(ProgramacionServicio, on_delete=models.CASCADE)
    impuestos_aplicados = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} para {self.id_cliente.nombre_empresa}"

class MaterialLimpieza(models.Model):
    nombre_material = models.CharField(max_length=255)
    descripcion = models.TextField()
    stock_actual = models.IntegerField()
    fecha_caducidad = models.DateField()
    id_proveedor = models.IntegerField() # Assuming a simple integer for now
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_material = models.CharField(max_length=50)
    ubicacion_almacen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_material

class UsoMaterial(models.Model):
    id_programacion = models.ForeignKey(ProgramacionServicio, on_delete=models.CASCADE)
    id_material = models.ForeignKey(MaterialLimpieza, on_delete=models.CASCADE)
    cantidad_usada = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    id_empleado_registro = models.ForeignKey(EmpleadoLimpieza, on_delete=models.CASCADE)
    comentarios_uso = models.TextField()

    def __str__(self):
        return f"Uso de {self.id_material.nombre_material} en servicio {self.id_programacion.id}"
