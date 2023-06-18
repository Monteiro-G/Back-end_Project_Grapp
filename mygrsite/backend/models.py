from django.db import models
# Create your models here.
class Cliente(models.Model):
    codclient = models.AutoField(primary_key=True)
    cliente =  models.CharField(max_length=100)
    fentasia = models.CharField(max_length=100)
    cpfcnpj = models.CharField(max_length=18)
    ie = models.CharField(max_length=18)
    atividade = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    codcidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    pais = models.CharField(max_length=50)
    dtcadastro = models.DateField()
    dtultatualizacao = models.DateTimeField(auto_now=True)
    dtultcompra = models.DateField()
    categoriaclient = models.CharField(max_length=50)
    observacao = models.TextField()

def __str__(self):
    return self.cliente

class Meta:
    db_table = 'grclient'
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'

  
class PedidoCompra(models.Model):
    codpedcompr = models.AutoField(primary_key=True)
    codfornec = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    codprod = models.ForeignKey('Produto', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dtemissao = models.DateField()
    vlpedido = models.DecimalField(max_digits=10, decimal_places=2)
    statusped = models.CharField(max_length=20)
    def __str__(self):
        return f"Pedido de Compra {self.codpedcompra}"
    
    class Meta:
        db_table = 'grpedcompra'
        verbose_name = 'Pedido de Compra'
        verbose_name_plural = 'Pedidos de Compra'


class Produto(models.Model):
    codprod = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    unidade = models.CharField(max_length=20)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    codmarca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    caracteristicas = models.TextField()
    codfornec = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    codsecao = models.ForeignKey('Secao', on_delete=models.CASCADE)
    codbarra = models.CharField(max_length=20)
    dtcadastro = models.DateTimeField(auto_now_add=True)
    dtultatualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'grprodut'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

class Marca(models.Model):
    codmarca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    dtcadastro = models.DateField()
    dtultatualizacao = models.DateField()

    def __str__(self):
        return self.marca

    class Meta:
        db_table = 'grmarca'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Fornecedor(models.Model):
    codfornec = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    codcidade = models.IntegerField()
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    dtcadastro = models.DateTimeField(auto_now_add=True)
    dtultatualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'grfornec'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

class Estoque(models.Model):
    codest = models.AutoField(primary_key=True)
    codprod = models.IntegerField()
    quantidade = models.IntegerField()
    codfornec = models.IntegerField()
    precovenda = models.DecimalField(max_digits=10, decimal_places=2)
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    dtcadastro = models.DateTimeField(auto_now_add=True)
    dtultatualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.codest)

    class Meta:
        db_table = 'grest'
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'

class Secao(models.Model):
    codsecao = models.AutoField(primary_key=True)
    secao = models.CharField(max_length=100)
    dtcadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.secao

    class Meta:
        db_table = 'grsecao'
        verbose_name = 'Seção'
        verbose_name_plural = 'Seções'


class CabecarioPedido(models.Model):
    numped = models.AutoField(primary_key=True)
    dtped = models.DateTimeField(auto_now_add=True)
    codclient = models.IntegerField()
    vlpedido = models.DecimalField(max_digits=10, decimal_places=2)
    vltabelaped = models.DecimalField(max_digits=10, decimal_places=2)
    vlcustoped = models.DecimalField(max_digits=10, decimal_places=2)
    statusped = models.CharField(max_length=50)
    dtentrega = models.DateField()
    numitens = models.IntegerField()
    codusu = models.IntegerField()
    codcob = models.CharField(max_length=10)
    dtultatualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.numped)

    class Meta:
        db_table = 'grcabped'
        verbose_name = 'Cabeçario do Pedido'
        verbose_name_plural = 'Cabeçario dos Pedidos'
        
class ItensPedido(models.Model):
    dtped = models.DateTimeField(auto_now_add=True)
    numseq = models.IntegerField()
    numped = models.ForeignKey('CabecarioPedido', on_delete=models.CASCADE)
    codprod = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    statusped = models.CharField(max_length=50)
    prevenda = models.DecimalField(max_digits=10, decimal_places=2)
    pretabela = models.DecimalField(max_digits=10, decimal_places=2)
    custoitem = models.DecimalField(max_digits=10, decimal_places=2)
    codclient = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    codusu = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    percdescont = models.IntegerField()
    prazomedio = models.IntegerField()
    dtaltatualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'gritemped'
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
        unique_togethrt = ('numseq','numped','codprod')
   
    def __str__(self):
        return f'Pedido: {self.numped} - Sequencia: {self.numseq} - Produto: {self.codprod}'

class Cobranca(models.Model):
    codcob = models.CharField(primary_key=True, max_length=5)
    Cobranca = models.CharField(max_length=10)
    descricao = models.CharField(max_length=250)

    class Meta:
        db_table = 'grcob'
        verbose_name = 'Cobrança'
        verbose_name_plural = 'Cobranças'
    
    def __str__(self):
        return self.cobranca

class Usuario(models.Model):
    codusu = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    dtcadastro = models.DateTimeField(auto_now_add=True)
    dtexclusao = models.DateField(null=True, blank=True)
    dtultatualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'grusuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    codcidade = models.AutoField(primary_key=True)
    cidade = models.CharField(max_length=100)
    codIBGE = models.IntegerField()
    estado = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=10, null=True, blank=True)
    dtcadastro = models.DateTimeField(auto_now_add=True)
    dtaltatualizacao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cidade
    
    class Meta:
        db_table = 'grcidade'
        verbose_name = ' Cidade'
        verbose_nome_plural = 'Cidades'