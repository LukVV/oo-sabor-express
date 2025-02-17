from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliacao'}'  )
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {restaurante.media_avaliacoes}' )
    
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property   
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media
    
    
    def adicionar_no_cardapio(self, item):
        # Verificando se o item que estamos inserindo 
        # for uma instancia do ItemCardapio ou herdar da mesma
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
     
    @property        
    def exibir_cardapio(self):
        print (f'Cardapio do Restaurante {self._nome}\n')
        #Enumerate devolve duas informações o index e o proprio item da lista
        #O Start é usado para determinar qual o index do primeito item que por padrão é 0
        for i,item in enumerate(self._cardapio, start=1):
            mensagem = f'{i}. Nome:{item._nome} | Preço: R${item._preco}'
            
            if hasattr(item, '_descricao'):
                mensagem += f' | Estoque: {item._descricao}'
            else:
                mensagem += f' | Tamanho: {item._tamanho}'
            
            print (mensagem)
            
        
        

        
        
