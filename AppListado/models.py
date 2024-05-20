from datetime import date
from django.db import models

# TABLA DE USUARIOS DE PRUEBA
class Users(models.Model):
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        managed = False
        db_table = 'users'

# TABLA PARA EL LISTADO DE REMATES
class Remates(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    departamento = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    juzgado = models.CharField(max_length=100)
    numero_proceso = models.CharField(max_length=25)
    avaluo = models.DecimalField(max_digits=15, decimal_places=2)
    valor_subasta = models.DecimalField(max_digits=15, decimal_places=2)
    tipo_bien = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    placa_vehiculo = models.CharField(max_length=25, blank=True, null=True)
    matricula_inmobiliaria = models.CharField(max_length=25, blank=True, null=True)
    referencia_catastral = models.CharField(max_length=25, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"${self.numero_proceso}"