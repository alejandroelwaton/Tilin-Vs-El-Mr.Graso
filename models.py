import time
import os
import readchar


class Player:
    def __init__(self, name:str):
        self.name = name
        self.health = 100
        self.defense = 5
        self.energy = 25
        self.damage = 10
        self.inventory = []
        self.ubication = 'Casa'
        


    def encontrar_espada(self, espada):
        print(f'\nTe has encontrado una "{espada.name}"')
        print('Tu daño ha aumentado en: ' + str(espada.filo))
        temp = self.damage
        self.damage += espada.filo
        self.inventory.append(espada)
        print(f'Daño: {temp} -> {self.damage}')
        time.sleep(4)


    def encontrar_escudo(self, escudo):
        print(f'\nTe has encontrado un "{escudo.name}"')
        print('Tu defensa ha aumentado en: ' + str(escudo.defensa))
        temp = self.defense
        self.defense += escudo.defensa
        self.inventory.append(escudo)
        print(f'Escudo: {temp} -> {self.defense}')
        time.sleep(4)


    def encontrar_pocion(self, pocion):
        print(f'Te has encontrado una {pocion.name}')
        print(f'Esta pocion regenera tu Vida en {pocion.regeneracion}')
        self.inventory.append(pocion)
        time.sleep(4)

    
    def mostrar_inventario(self):
        print('\n=====Objetos De Tu Inventario=====')
        for objetos in self.inventory:
            print(f'- {objetos.name}')
            


    def mostrar_ubicacion(self):
        print(self.ubication.name)



    def moverse(self, lugar: str):
        print(f'Te encuentras en: {lugar.name}')
        self.ubication = lugar


class Enemy:
    def __init__(self, name:str, difficulty: int):
        self.name = name
        self.health = 25 * difficulty
        self.defense = 5
        self.energy = 25
        self.damage = 10
        

class Scene:
    def __init__(self, name: str):
        self.name = name


    def crear_enemigo(self, name: str, difficulty: int):
        return Enemy(name + ' de ' + self.name, difficulty)


class Persona:
    def __init__(self, name: str):
        self.name = name

    
    def decir(self, texto: str):
        print(f'{self.name}: {texto}')
        time.sleep(4)


class Item:
    def __init__(self, name: str, filo: int=0, defensa: int=0, regeneracion: int =0):
        self.name = name
        self.filo = filo
        self.defensa = defensa
        self.regeneracion = regeneracion