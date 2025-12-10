from django import forms
from .models import (
    ClienteLimpieza, ServicioLimpieza, EmpleadoLimpieza, 
    ProgramacionServicio, FacturaLimpieza, MaterialLimpieza, UsoMaterial
)

class ClienteLimpiezaForm(forms.ModelForm):
    fecha_inicio_contrato = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ClienteLimpieza
        fields = '__all__'

class ServicioLimpiezaForm(forms.ModelForm):
    class Meta:
        model = ServicioLimpieza
        fields = '__all__'

class EmpleadoLimpiezaForm(forms.ModelForm):
    fecha_contratacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = EmpleadoLimpieza
        fields = ['nombre', 'apellido', 'dni', 'fecha_contratacion', 'salario_hora', 'turno', 'telefono', 'email', 'certificaciones_seguridad']

class ProgramacionServicioForm(forms.ModelForm):
    fecha_programada = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora_inicio = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    hora_fin = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = ProgramacionServicio
        fields = '__all__'

class FacturaLimpiezaForm(forms.ModelForm):
    fecha_emision = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_vencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = FacturaLimpieza
        fields = '__all__'

class MaterialLimpiezaForm(forms.ModelForm):
    fecha_caducidad = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = MaterialLimpieza
        fields = '__all__'

class UsoMaterialForm(forms.ModelForm):
    class Meta:
        model = UsoMaterial
        fields = '__all__'
