from django.shortcuts import render

# As Views criadas a baixo listam os registros de cada tabela no banco de dados através dos modelos criados no models.py
from .models import Cliente, PedidoCompra, Produto, Marca, Fornecedor, Estoque, Secao, CabecarioPedido, ItensPedido, Cobranca, Usuario, Cidade

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def lista_pedidos_compras(request):
    pedidoscomp = PedidoCompra.objects.all()
    return render(request, 'lista_pedidos_compras.html', {'pedidoscomp': pedidoscomp})

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'lista_marcas.html', {'marcas': marcas})

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'lista_fornecedores.html', {'fornecedores': fornecedores})

def lista_estoques(request):
    estoques = Estoque.objects.all()
    return render(request, 'lista_estoques.html', {'estoques': estoques})

def lista_secoes(request):
    secoes = Secao.objects.all()
    return render(request, 'lista_secoes.html', {'secoes': secoes})

def lista_cabecalho_pedidos(request):
    cabecalhos = CabecarioPedido.objects.all()
    return render(request, 'lista_cabecalhos.htm', {'cabecalhos': cabecalhos})

def lista_itens_pedidos(request):
    itens = ItensPedido.objects.all()
    return render(request, 'lista_itens.html', {'itens': itens})

def lista_cobrancas(request):
    cobrancas = Cobranca.objects.all()
    return render(request, 'lista_cobrancas', {'cobrancas': cobrancas})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html',{'usuarios': usuarios})

def lista_cidades(request):
    cidades = Cidade.objects.all()
    return render(request, 'lista_cidades.html',{'cidades': cidades})

# As Views criadas a baixo gravam os dados informados pelo usuario

