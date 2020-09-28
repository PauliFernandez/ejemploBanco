#! /usr/bin/python3
#Ponemos a disposición de este archivo las dos clases que utilizaremos.
from cajaAhorro import CajaAhorro
from cuentaCorriente import CuentaCorriente

#Solicitamos datos:
nombre = input("Ingrese el nombre del titular de la cuenta ")
saldo = int(input("Ingrese el depósito inicial "))
tipo = int(input("Ingrese el tipo de cuenta: 1:Caja de Ahorro 2:CtaCte "))
tope = int(input("Ingrese el tope de extracción/descubierto "))

#Según el valor recibido en tipo, instanciamos de CajaAhorro o CuentaCorriente.
if tipo == 1:
    cuenta = CajaAhorro(nombre, saldo, tope)
elif tipo == 2:
    cuenta = CuentaCorriente(nombre, saldo, tope)
else:
    print("Error: ingrese el tipo 1 o 2")
    exit()

#Este bucle nos permite realizar muchas operaciones.
continuar = "s"
while continuar == "s" or continuar == "S":
    print("El saldo de la cuenta es $", cuenta.saldo)
    #Solicitamos el tipo de operación y el monto.
    operacion = input("Ingrese el tipo de operación (D/E)")
    monto = int(input("Ingrese el monto de la operación"))

    #Invocamos al método polimórfico correspondiente.
    if operacion == "D" or operacion == "d":
        print(cuenta.depositar(monto))
    elif operacion == "E" or operacion == "e":
        print(cuenta.extraer(monto))
    else:
        print("Error: tipo de operación errónea")
    continuar = input("¿Realizar otra operación? (S/N) ")

#Para finalizar, mostramos el saldo con el que quedó la cuenta:
print("El saldo final de la cuenta es $", cuenta.saldo)
