'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que 
es una persona) y cantidad (puede tener decimales). El titular será obligatorio 
y la cantidad es opcional. Crear los siguientes métodos para la clase: 
 Un constructor, donde los datos pueden estar vacíos. 
 Los setters y getters para cada uno de los atributos. El atributo no se puede 
modificar directamente, sólo ingresando o retirando dinero. 
 mostrar(): Muestra los datos de la cuenta. 
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad 
introducida es negativa, no se hará nada. 
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en 
números rojos.
'''
from Ejercicio06 import ingresoPersona
from Ejercicio06 import Persona


class Cuenta(Persona):
     def __init__(self,nombre,cantidad):
          self.titular = nombre
          self.cantidad = cantidad

     def set_titular(self,titular):
         self.titular = titular

     def set_cantidad(self,cantidad):
         self.cantidad = cantidad

     def get_titular(self):
         return self.titular

     def get_cantidad(self):
         return self.cantidad

     def mostrar(self,titular,cantidad):
         print('\n Mostrando datos de la cuenta\n')
         input(f'Titular: {self.titular} \nDinero en cuenta: {self.cantidad}' )

     def ingresar(self,cantidad):
          dinero=float(input('Por favor ingrese el monto a depositar: '))
          if dinero > 0:
               cantidad = self.cantidad + dinero
               self.cantidad = cantidad

     def retirar(self,cantidad):
          dinero=float(input('Por favor ingrese el monto a retirar: '))
          cantidad = self.cantidad - dinero
          self.cantidad = cantidad

    
def operarCuenta (mi_cuenta):
     operar='n'
     while operarCuenta!='S' and operar!='s':

          menu= '\nQue desea hacer:\n Mostrar los datos de la cuenta presione "M"\n Ingresar dimero en la cuenta pulse "I".\n Retirar dimero en la cuenta pulse "R".\n Salir pulse "S".\n Ingrese su respuesta, verifique y luego presione enter '
          operar = input(menu)

          if operar== 'M' or operar== 'm':
               mi_cuenta.mostrar(mi_cuenta.titular,mi_cuenta.cantidad)

          if operar== 'I' or operar== 'i':
               mi_cuenta.ingresar(mi_cuenta.cantidad)
               
          if operar== 'R' or operar== 'r':
               mi_cuenta.retirar(mi_cuenta.cantidad)

     return()

print ('#'*40,  'Inicio', '#'*40,'\n')
    
mi_persona=ingresoPersona()
mi_cuenta=Cuenta(mi_persona.nombre,0)
operarCuenta(mi_cuenta)
    
print ('\n','#'*40,' FIN ', '#'*40)