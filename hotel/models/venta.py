from django.db import models
from core.models import User
from .cliente import Cliente
from .docType import Doc_Type


class Venta(models.Model):

    direccion = models.CharField(max_length=15)
    numDoc = models.CharField(max_length=15)
    estado = models.BooleanField(default=False)
    igv = models.CharField(max_length=5)
    serie = models.CharField(max_length=15)
    numero_reservacion = models.IntegerField()
    vendedor = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True, null=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    doc_type = models.ForeignKey(Doc_Type)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % (self.vendedor)
