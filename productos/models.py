from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField()
    precio = models.DecimalField()
    cantidad = models.IntegerField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre   
