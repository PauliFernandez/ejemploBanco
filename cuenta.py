#! /usr/bin/env python3

class Cuenta:
    """ Cuenta bancaria """

    def __init__(self, titular, saldoInicial): 
        self.titular = titular
        self.saldo = saldoInicial

    def depositar(self, monto):
        self.saldo = self.saldo + monto
        return "Depósito exitoso. Saldo $" + str(self.saldo)

    def extraer(self,monto):
        self.saldo = self.saldo - monto
        return "Extracción exitosa. Saldo $" + str(self.saldo)    

