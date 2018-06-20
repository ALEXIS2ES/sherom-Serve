from django.db import models


class Doc_Type(models.Model):

    tipo_documento = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Doc_Type"
        verbose_name_plural = "Doc_Types"

    def __str__(self):
        return '%s' % (self.tipo_documento)
