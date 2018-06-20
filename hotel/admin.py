from django.contrib import admin
from hotel.models.reserva import Reserva
from hotel.models.habitacion import Habitacion
from hotel.models.pago import Forma_de_pago
from hotel.models.cliente import Cliente
from hotel.models.venta import Venta
from hotel.models.docType import Doc_Type
from hotel.models.area import Area
from hotel.models.detalleVenta import Detalle_Venta
from hotel.models.trabajador import Trabajador
from hotel.models.tipoHabitacion import Tipo_Habitacion

# Register your models here.
admin.site.register(Reserva)
admin.site.register(Habitacion)
admin.site.register(Forma_de_pago)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Doc_Type)
admin.site.register(Area)
admin.site.register(Detalle_Venta)
admin.site.register(Trabajador)
admin.site.register(Tipo_Habitacion)
