# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *

class ReglaValidacion:
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        if self.regla.es_valida(clave):
            return True
        else:
            return False

class ReglaValidacionGanimedes(ReglaValidacion):
    pass

class ReglaValidacionCalisto(ReglaValidacion):
    pass