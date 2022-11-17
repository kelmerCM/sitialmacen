from django.urls import path
from Apps.productos.views import ProductoView


app_name = "productos"
urlpatterns = [
    path('', ProductoView.as_view()),
]
