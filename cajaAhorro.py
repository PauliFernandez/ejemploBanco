#! /usr/bin/python3

class CajaAhorro:
    """Cuenta bancaria que tiene un tope de extracción (no se puede extraer
    más de cierto monto por cada operación"""

    def __init__(self, titular, saldoInicial, topeExtraccion):
        self.titular = titular
        self.saldo = saldoInicial
        self.topeExtraccion = topeExtraccion

    def extraer(self, monto):
        if monto > self.topeExtraccion or monto > self.saldo:
            return "Error. Excede tope de extracción o saldo"
        else:
            self.saldo = self.saldo - monto
            return "Extracción exitosa. Saldo $" + str(self.saldo)    
    
    def depositar(self, monto):
        self.saldo = self.saldo + monto
        return "Depósito exitoso. Saldo $" + str(self.saldo)

