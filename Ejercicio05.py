'''
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir
una cadena de texto en su valor numérico, escriba una función get_int() que lea 
un valor entero del usuario y lo devuelva, iterando mientras el valor no sea 
correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.
'''
def get_int():
    
    repetir=0
    cont=0 
    while repetir==0:
               
        valor_ingresado=input('Por favor ingrese un valor ')
        try:
            valor = int(valor_ingresado)
            repetir=1
        except ValueError:
            cont=cont+1
            print('no es un numero')

    return(cont,valor)
       

 




print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
while (continuar=='s' or continuar=='S'):
    valor=get_int()
    cont=valor[0]
    numero=valor[1]
    if cont<5:
        print(f'El valor ingresado es el número: {numero}')
    else:
        print(f'Por fin escribiste un número el número fue: {numero}')




    continuar = input('Desea ejecutar de nuevo el programa pulse la tecla S y enter ')
print ('\n','#'*40,' FIN ', '#'*40)