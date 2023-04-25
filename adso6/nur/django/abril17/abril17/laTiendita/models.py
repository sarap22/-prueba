from django.db import models

# Create your models here.
class productos(models.Model):
    nombre=models.CharField(max_length=20)
    codigo=models.CharField(max_length=1)
    tipo=models.CharField(max_length=20)
    precio=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)

class clientes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.CharField(max_length=20)
    celular=models.CharField(max_length=10)
    documento=models.CharField(max_length=15)



