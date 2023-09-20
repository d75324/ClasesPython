# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es la Persona de
# ejemplo1_Persona) y cantidad, que es el total de pesos en cuenta y que puede tener decimales.
# El titular será obligatorio pero la cantidad puede ser cero.

# Construir los siguientes métodos para la clase Cuenta:

# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta.
# Si la cantidad ingresada es negativa, no se hará nada y se enviará un mensaje de error.
# retirar(cantidad): retira una cantidad de la cuenta.
# La cuenta puede quedar en rojo y en ese caso se debe informar.

from ejemplo1_Persona import *

class Cuenta(Persona):
    def __init__(self, nombre, edad, dni, cantidad):
        super().__init__(nombre, edad, dni)
        self.cant = cantidad
    
    def mostrar_cuenta(self):
        print (f'Nombre:          {self.nom}\nTotal en Cuenta: {self.cant} USD')

    def ingresar(self, ingreso):
        self.ing = ingreso
        if int(self.ing) > 0:
            y = int(self.cant) + int(self.ing)
            print(f'Ha ingresado {self.ing} USD.\nEl total de su cuenta es ahora de {y} USD')
            self.cant = y
        else:    
            print('Cabeza, no podés ingresar un monto negativo.')
    
    def retirar(self, retiro):
        self.ret = retiro
        ro = int(self.cant) - int(self.ret)
        if int(self.ret) > int(self.cant):
            print(f'La operación se completó. Tiene un saldo negativo de {ro}')
        else:
            print(f'La operación se completó. Su saldo es de {ro}')

#r = input('Indique el total que desea ingresar: ')
#anoder = Cuenta("Juan", 15, 22555777, 2373)
#anoder.ingresar(r)
#p = input('Indique el monto que desea retirar: ')
#anoder.retirar(p)
#anoder.mostrar_cuenta()