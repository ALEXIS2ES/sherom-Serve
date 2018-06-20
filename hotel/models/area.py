from django.db import models


class Area(models.Model):

    area = models.CharField(max_length=15)
    detalle_area = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self):
        return '%s' % (self.area)
