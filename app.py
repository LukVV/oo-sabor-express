from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato



restaurante = Restaurante('XFood', 'Japones')
bebida_suco = Bebida('Suco de Limão', 5.0, 'grande')
prato = Prato('Coxinha', 8, 'Coxinha com catupiry')
restaurante.adicionar_no_cardapio(bebida_suco)
restaurante.adicionar_no_cardapio(prato)




def main():
    restaurante.exibir_cardapio
    prato.aplicar_desconto()
    restaurante.exibir_cardapio

if __name__ == '__main__':
    main ()