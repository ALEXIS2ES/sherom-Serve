from django.db import models
from .tipoHabitacion import Tipo_Habitacion


class Habitacion(models.Model):

    estado = models.BooleanField(default=False)
    numero = models.CharField(max_length=15)
    piso = models.CharField(max_length=10)
    precio_diario = models.FloatField(default=0.0)
    tipo_habitacion = models.ForeignKey(Tipo_Habitacion, blank=True, null=True)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return '%s' % (self.tipo_habitacion)
