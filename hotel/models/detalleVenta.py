from django.db import models
from .venta import Venta


class Detalle_Venta(models.Model):

    producto = models.CharField(max_length=15)
    cantidad = models.IntegerField(default=0)
    importe = models.FloatField(default=0.0)
    servicio_ofrecido = models.CharField(max_length=15)
    precio_unitario = models.FloatField(default=0.0)
    precio_total = models.FloatField(default=0.0)
    venta = models.ForeignKey(Venta)

    class Meta:
        verbose_name = "DetalleVenta"
        verbose_name_plural = "DetalleVentas"

    def __str__(self):
        return '%s' % (self.producto)
