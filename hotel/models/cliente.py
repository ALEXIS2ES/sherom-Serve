from django.db import models


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    apellido_paterno = models.CharField(max_length=60)
    apellido_materno = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    edad = models.CharField(max_length=60)
    dni = models.CharField(max_length=8)
    email = models.EmailField(max_length=60, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido_paterno, )
