from django.db import models


class Forma_de_pago(models.Model):

    forma_pago = models.CharField(max_length=15)
    tipo_moneda = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Forma_de_pago"
        verbose_name_plural = "Forma_de_pagos"

    def __str__(self):
        return '%s' % (self.formaPago)
