from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from Apps.clientes.models import Cliente
from Apps.clientes.serializers import ClienteSerializer
from rest_framework import generics

# Create your views here.


class ClienteList(APIView):
    """
    Lista de Clientes
    """

    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        #data = {"results": list(clientes.values("nombreVliente","direccionCliente","telefonoCliente","correoCliente","passwordCliente"))}
        #print(data)
        #return JsonResponse(data)
        #print(clientes)
        return Response({"clientes":serializer.data})

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

