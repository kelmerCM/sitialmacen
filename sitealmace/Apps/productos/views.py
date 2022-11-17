from rest_framework.response import Response
from rest_framework.views import APIView

from Apps.productos.models import Producto, TipoProducto

class ProductoView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        return Response({"productos": productos})
