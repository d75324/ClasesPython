# Crear CuantaJoven que deriva de ejemplo1_Cuenta. 
# Además del titular y la cantidad, esta clase debe ofrecer una bonificación,
# que estará expresada en tanto por ciento, a través de un texto que lo informe.

# Construir los siguientes métodos para la clase:
# Un constructor
# Crear el método esTitularValido() que devuelve True si el titular es mayor de edad
# pero menor de 25 años y False en caso contrario.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven”, monto disponble y 
# la bonificación de la cuenta.

from ejemplo1_Persona import *
from ejemplo1_Cuenta import *

class CuentaJoven(Cuenta):
    def __init__(self, nombre, edad, dni, cantidad, bonificacion):
        super().__init__(nombre, edad, dni, cantidad)
        self.boni = bonificacion
    
    def esTitularValido(self):
        if 18 < int(self.eda) < 25:
            print(f'True: Bonificación de Cuenta Joven: {self.boni}%')
        else:
            print('False: No pueede acceder a Cuenta Joven')

    def mostrarr(self):
        if 18 < int(self.eda) < 25:
            print(f'Hola {self.nom}, tu saldo es de {self.cant} USD.\nDispones de una bonificación de {self.boni}%.')
        else:
            print(f'Hola {self.nom}, tu saldo es de {self.cant} USD.')


lasto = CuentaJoven("Roberto", 19, 22777444, 1734, 18)
print('')
lasto.esTitularValido()
print('')
lasto.mostrarr()
print('')