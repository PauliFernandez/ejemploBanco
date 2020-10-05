#! /usr/bin/python3

from cajaAhorro import CajaAhorro

class CajaAhorroEspecial(CajaAhorro):

    def __init__(self,titular,saldo_inicial,tope_extraccion,deposito_minimo):
        self.deposito_minimo = deposito_minimo
        super().__init__(titular, saldo_inicial, tope_extraccion)

    def depositar(self, monto):
        if (monto < self.deposito_minimo):
            return "Error. No alcanza el mínimo necesario"
        else:
            return super().depositar(monto)

