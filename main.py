from models import *


def introduccion(mainPlayer):
    max = Persona('Max')
    max.decir('Ohhh, pero si es el mismisimo ' + mainPlayer.name + ', que gusto verte.')
    max.decir('Toma, tu abuelo queria que de dejara una espada y un escudo, lo necesitarás')
    espada = Item('Espada de madera', filo=5)
    mainPlayer.encontrar_espada(espada)
    escudo = Item('Escudo de madera', defensa=10)
    mainPlayer.encontrar_escudo(escudo)


def new_player():
    nombre = input("Cual es tu nombre: ")
    print(f'''Te encuentras tranquilo en tu casa cuando de repente escuchas sonidos raros fuera de tu casa, te acercas a la ventana y logras ver una carta. \nAbres la puerta y lo tomas, La carta dice...: ''')
    time.sleep(8)
    print(f"""
De tu abuelo: 

    Querido {nombre} soy tu abuelo,
    he escrito esta carta antes de partir, 
    mi ultimo deseo es que desmanteles la secta grasosa liderada por Mr.Graso""")
    time.sleep(7)
    print("\n    PD: Cuidate mucho, te recibira mi amigo Max en Mi antigua casa.\n")
    time.sleep(3)

    return Player(nombre)


def main():
    os.system("cls")
    casaDeAbuelo = Scene('Casa Del Abuelo')
    mainPlayer = new_player()
    mainPlayer.moverse(casaDeAbuelo)
    introduccion(mainPlayer)
    mainPlayer.mostrar_ubicacion()
    

if __name__ == "__main__":
    main()