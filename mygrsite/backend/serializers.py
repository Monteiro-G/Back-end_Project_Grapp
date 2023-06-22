from rest_framework import serializers
from .models import Cliente, PedidoCompra, Produto, Marca, Fornecedor, Estoque, Secao, CabecarioPedido, ItensPedido, Cobranca, Usuario, Cidade

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCompra
        fields = '__all__'
