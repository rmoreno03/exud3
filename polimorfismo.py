# polimorfismo.py

import math


class EquiFigura:
    def __init__(self, longitudLados):
        self.__longitudLados = longitudLados

    def get_longitud_lados(self):
        return self.__longitudLados

    def set_longitud_lados(self, longitudLados):
        self.__longitudLados = longitudLados

    def toString(self):
        return f'EquiFigura[longitudLados={self.__longitudLados}]'


class TrianguloEquilatero(EquiFigura):
    def getPerimetro(self):
        return 3 * self.get_longitud_lados()

    def getArea(self):
        lado = self.get_longitud_lados()
        return (math.sqrt(3) / 4) * (lado ** 2)


class Cuadrado(EquiFigura):
    def getPerimetro(self):
        return 4 * self.get_longitud_lados()

    def getArea(self):
        lado = self.get_longitud_lados()
        return lado ** 2


def getPerimetroFigura(figura):
    return figura.getPerimetro()


def getAreaFigura(figura):
    return figura.getArea()


te1 = TrianguloEquilatero(3)
cu1 = Cuadrado(4)

print(f"Perímetro de te1: {getPerimetroFigura(te1)}")
print(f"Área de te1: {getAreaFigura(te1)}")

print(f"Perímetro de cu1: {getPerimetroFigura(cu1)}")
print(f"Área de cu1: {getAreaFigura(cu1)}")
