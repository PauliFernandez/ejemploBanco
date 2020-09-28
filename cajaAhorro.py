#! /usr/bin/python3

from cuenta import Cuenta

class CajaAhorro(Cuenta):
    """Cuenta bancaria que tiene un tope de extracción (no se puede extraer
    más de cierto monto por cada operación"""

    def __init__(self, titular, saldoInicial, topeExtraccion):
        self.topeExtraccion = topeExtraccion
        super().__init__(titular,saldoInicial)

    def extraer(self, monto):
        if monto > self.topeExtraccion or monto > self.saldo:
            return "Error. Excede tope de extracción o saldo"
        else:
            return super().extraer(monto)
    

