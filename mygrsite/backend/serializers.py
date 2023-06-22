from rest_framework import serializers
from .models import Cliente, PedidoCompra, Produto, Marca, Fornecedor, Estoque, Secao, CabecarioPedido, ItensPedido, Cobranca, Usuario, Cidade

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCompra
        feilds = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'

class SecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        fields = '__all__'

class CabecarioPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabecarioPedido
        fields = '__all__'

class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'

class CobrancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobranca
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'