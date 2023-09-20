# Crear una clase llamada Persona con atributos nombre, edad y DNI.
# Construir los siguientes métodos para la clase:
# mostrar(): Muestra los datos de la persona en el formato que mas te guste.
# esMayorDeEdad(): Que devuelva un valor lógico indicando si es mayor de edad.

class Persona():
    def __init__(self, nombre, edad, dni):
        self.nom = nombre
        self.eda = edad
        self.dni = dni
    
    def mostrar(self):
        print (f'Nombre: {self.nom}\n  Edad: {self.eda}\n   DNI: {self.dni}')

    def esMayorDeEdad(self):
        if self.eda > 18:
            print("True")
        else:
            print("False")

#perso = Persona("Juan", 15, 22555777)
#perso2 = Persona("Ricardo", 27, 33444555)
#print(perso.dni)
#perso2.esMayorDeEdad()
#perso2.mostrar()