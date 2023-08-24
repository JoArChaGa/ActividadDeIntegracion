'''
Escribir una función que calcule el mínimo común múltiplo entre dos números.
'''

print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
while (continuar=='s' or continuar=='S'):
    num1 = int (input("Por favor ingrese el 1º numero: "))
    num2 = int (input("Por favor ingrese el 2º numero: "))
    print ('El minimo con un multiplo entre ', num1, ' y ', num2, ' es ')
    mcm=1
    cont=2
    while (cont <= num1):
        if num1 % cont == 0:
            num1 =int (num1 / cont)        
            mcm = mcm * cont
            if num2 % cont == 0 :
                num2=int (num2/cont)
            cont=1
        cont=cont+1

    while (cont <= num2):
        if num2 % cont == 0:
            num2 =int (num2 / cont)        
            mcm = mcm * cont
            cont=1
        cont=cont+1

    print (mcm)
    continuar = input('Desea ejecutar de nuevo el programa pulse la tecla S y enter ')
print ('\n','#'*40,' FIN ', '#'*40)