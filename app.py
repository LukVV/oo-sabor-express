from modelos.restaurante import Restaurante


restaurante1 = Restaurante('tiktok', 'Dançante')
restaurante1.receber_avaliacao('Nunes', 9)
restaurante1.receber_avaliacao('Fabricia', 7)
restaurante2 = Restaurante('AmricanFood', 'Comida Americana')
restaurante3 = Restaurante('XFood', 'Japones')

restaurante2.alternar_estado()



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main ()