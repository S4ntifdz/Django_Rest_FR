from django.urls import path
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import InmuebleListAV, InmuebleDetalleAV
urlpatterns = [
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    #este path representa la lista que devuelve el pedido de inmuebles
    #inmueble_list es la funcnion DEF que va a procesar el request que va a ingresar por el endpoint 'list/'
    #debo crear dentro del archivo views.py
    path('<int:pk>', InmuebleDetalleAV.as_view(), name='inmueble-detalle'),
]
