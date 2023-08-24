'''
Escribir una función que calcule el máximo común divisor entre dos números
'''
def Multiplo (num):
    inicio = num
    multiplos = []
    for contador in range(inicio, 1, -1):
        if num % contador == 0:
          multiplos.append(contador)
    return (multiplos)


print ('@'*40,  'Inicio', '@'*40,'\n')
continuar= ('s')
while (continuar=='s' or continuar=='S'):
    num1 = int (input("Por favor ingrese el 1º numero: "))
    num2 = int (input("Por favor ingrese el 2º numero: "))
    multiplosNum1 = Multiplo(num1)
    multiplosNum2 = Multiplo(num2)
    finFor1=0
    for i in range(len(multiplosNum1)):
        for i2 in range(len(multiplosNum2)):
            if multiplosNum1[i]==multiplosNum2[i2]:
                print ('El máximo con un divisor entre ', num1, ' y ', num2, ' es ',multiplosNum1[i])
                finFor1=1
                break
        if finFor1==1:
                break
    continuar = input('Desea ejecutar de nuevo el programa pulse la tecla S y enter ')
print ('\n','#'*40,' FIN ', '#'*40)