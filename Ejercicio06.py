'''
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya 
los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las 
entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:
     def __init__(self, nombre, edad, DNI):
          self.nombre = nombre
          self.edad = edad
          self.DNI = DNI

     #Setters

     def set_nombre(self,nombre):
         self.nombre = nombre

     def set_edad(self,edad):
          self.edad = edad
     
     def set_DNI(self,DNI):
         self.DNI = DNI

     # Getters

     def get_nombre(self):
         return self.nombre
     
     def get_edad(self):
         return self.edad
     
     def get_DNI(self):
         return self.DNI
         
     def mostrar(self):
         print(f'Mostrando persona \n {self.nombre} {self.edad} {self.DNI}' )
    
     def Es_mayor_de_edad(self):
          if self.edad > 17:
            return True
          else:
            return False


def ingresoPersona(): 
    continuar='s'
    nombre = str(input('Ingrese el nombre: '))

    while (continuar=='s' or continuar=='S'):
        edad = int(input('Ingrese la edad: '))
        if edad < 0:
             print('La edad no puede ser negativa')
        else:
            continuar='n'

    continuar='s'
    while (continuar=='s' or continuar=='S'):
        DNI = int(input('Ingrese el DNI: '))
        if DNI < 10000000 or DNI > 99999999:
             print('Recuerde que el DNI debe tener 8 diguitos')
        else:
            continuar='n'

    mi_persona=Persona(nombre,edad,DNI)
    
    return (mi_persona)        


print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
while (continuar=='s' or continuar=='S'):
    mi_persona=ingresoPersona()
    
    
    impr = input('Desea ver los datos ingresados S/N ')
    if impr=='s' or impr=='S':
        mi_persona.mostrar()

    impr = input('Desea saber si es mayor de edad S/N ')
    if impr=='s' or impr=='S':
        mi_persona.Es_mayor_de_edad()


    continuar = input('Desea agregar otra persona pulse la tecla S y enter ')
print ('\n','#'*40,' FIN ', '#'*40)