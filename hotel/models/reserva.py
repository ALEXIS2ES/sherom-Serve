from django.db import models
from .cliente import Cliente


class Reserva(models.Model):

    costo_alojamiento = models.FloatField(blank=True, default=0.0)
    estado = models.BooleanField(default=False)
    tipo_reserva = models.CharField(blank=True, null=True, max_length=10)
    fecha_ingresa = models.DateTimeField(blank=True, null=True)
    fecha_reserva = models.DateTimeField(auto_now_add=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.tipo_reserva)
