from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato



restaurante = Restaurante('XFood', 'Japones')
bebida_suco = Bebida('Suco de Limão', 5.0, 'grande')
prato = Prato('Coxinha', 8, 'Coxinha com catupiry')




def main():
    print(bebida_suco)
    print(prato)

if __name__ == '__main__':
    main ()