from django.db import models

# Create your models here.


class Ingrediente(models.Model):
    id_ingredientes = models.CharField(primary_key=True, max_length=10)
    costo_ingrediente = models.DecimalField(max_digits=10, decimal_places=2)
    costo_mensual = models.DecimalField(max_digits=10, decimal_places=2)

class Empleados(models.Model):
    id_empleados             = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    labor  = models.CharField(max_length=20)

class Gastos(models.Model):
    costo_total = models.DecimalField(primary_key = True,max_digits=10, decimal_places=2)
    liquidaciones = models.DecimalField(max_digits=10, decimal_places=2)
    costo_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    arriendo_local = models.DecimalField(max_digits=10, decimal_places=2)

class Contratos(models.Model):
    id_contrato = models.CharField(primary_key=True,max_length=10)
    liquidaciones = models.DecimalField(max_digits=10, decimal_places=2)
