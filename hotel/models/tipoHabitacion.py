from django.db import models


class Tipo_Habitacion(models.Model):

    nombre = models.CharField(max_length=60, null=True, blank=True)
    foto = models.ImageField(blank=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Tipo_Habitacion"
        verbose_name_plural = "Tipo_Habitaciones"

    def __str__(self):
        return '%s' % (self.nombre)
