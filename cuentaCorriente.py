#! /usr/bin/env python3

class CuentaCorriente:
    """Cuenta bancaria que tiene un descubierto permitido (permiso para tener)
    saldo negativo en la cuenta"""

    def __init__(self, titular, saldoInicial, topeDescubierto):
        self.titular = titular
        self.saldo = saldoInicial
        self.topeDescubierto = topeDescubierto

    def extraer(self, monto):
        if monto > self.saldo + self.topeDescubierto:
            return "Error. Excede tope de descubierto"
        else:
            self.saldo = self.saldo - monto
            return "Extracción exitosa. Saldo $" + str(self.saldo)    

