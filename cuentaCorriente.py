#! /usr/bin/env python3

from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    """Cuenta bancaria que tiene un descubierto permitido (permiso para tener)
    saldo negativo en la cuenta"""

    def __init__(self, titular, saldoInicial, topeDescubierto):
        self.topeDescubierto = topeDescubierto
        super().__init__(titular,saldoInicial)

    def extraer(self, monto):
        if monto > self.saldo + self.topeDescubierto:
            return "Error. Excede tope de descubierto"
        else:
            return super().extraer(monto)


