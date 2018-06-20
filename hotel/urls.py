
from django.conf.urls import url, include
from rest_framework import routers
from .views.habitacion_view import HabitacionViewSet
from .views.cliente_view import ClienteViewSet
from .views.detalleVenta_view import Detalle_VentaViewSet
from .views.area_view import AreaViewSet
from .views.docType_view import Doc_TypeViewSet
from .views.pago_view import Forma_de_pagoViewSet
from .views.reserva_view import ReservaViewSet
from .views.trabajador_view import TrabajadorViewSet
from .views.venta_view import VentaViewSet
from .views.tipoHabitacion_view import Tipo_HabitacionViewSet

router = routers.DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'detalleVentas', Detalle_VentaViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'docTypes', Doc_TypeViewSet)
router.register(r'pagos', Forma_de_pagoViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'trabajadores', TrabajadorViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'tipoHabitaciones', Tipo_HabitacionViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
