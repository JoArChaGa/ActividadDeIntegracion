'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva 
clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea 
esta nueva clase, además del titular y la cantidad se debe guardar una bonificación 
que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase: 
 Un constructor.  Los setters y getters para el nuevo atributo. 
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero 
si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación 
de la cuenta.
'''
from Ejercicio06 import ingresoPersona
from Ejercicio06 import Persona
from Ejercicio07 import operarCuenta
from Ejercicio07 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad,bonificacion='0%'):
          super().__init__(titular, cantidad) 
          self.bonificacion = bonificacion

    def set_bonificacion(self,bonificacion):
         self.bonificacion = bonificacion

    def get_bonificacion(self):
         return self.bonificacion
    
    def es_titular_valido(self):
         if self.edad>18 and self.edad<25:
              self.bonificacion='5%'
         else:
              self.bonificacion='0%'


    def mostrar(self,titular,cantidad,bonificacion):
         print('\n Mostrando datos de la cuenta\n')
         input(f'Titular: {self.titular} \nDinero en cuenta: {self.cantidad} \nBonificacion: {self.bonificacion}' )

    
print ('#'*40,  'Inicio', '#'*40,'\n')
    
mi_persona=ingresoPersona()
mi_cuenta=Cuenta(mi_persona.nombre,mi_persona.edad,0)

operarCuenta(mi_cuenta)
    
print ('\n','#'*40,' FIN ', '#'*40)