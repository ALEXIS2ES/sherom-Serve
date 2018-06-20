from django.db import models
from .area import Area
from core.models import Person


class Trabajador(models.Model):

    cargo = models.CharField(max_length=15)
    estado = models.BooleanField(default=False)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    informacion_adicional = models.TextField(null=True, blank=True)
    area = models.ForeignKey(Area)
    person = models.OneToOneField(Person)

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        return '%s' % (self.cargo)
