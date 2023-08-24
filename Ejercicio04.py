'''
Escribir una función que reciba una cadena de caracteres y devuelva un 
diccionario con cada palabra que contiene y la cantidad de veces que aparece 
(frecuencia). Escribir otra función que reciba el diccionario generado con la 
función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
'''

def hacer_diccionario(cadena):
  lista_1= cadena.split()
  dicc_1={}
  for i in range (len(lista_1)):
    if lista_1[i] in dicc_1:
      dicc_1[lista_1[i]] +=1
    else:
      dicc_1[lista_1[i]]= 1
  return dicc_1


def hacer_tupla(diccionario):
    pal_frecuente= ''
    cant=0
    for keys,values in diccionario.items():
        if values > cant:
            cant= values
            pal_frecuente= keys
    return pal_frecuente,cant


print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
while (continuar=='s' or continuar=='S'):

    entrada=input('\n Ingrese su cadena de caracteres: ')
    print('\n', hacer_diccionario(entrada), '\n')
    print('\n', hacer_tupla(hacer_diccionario(entrada)) ,'\n')

    continuar = input('Desea ejecutar de nuevo el programa pulse la tecla S y enter ')
print ('\n','#'*40,' FIN ', '#'*40)