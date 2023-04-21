# Parcial

""""
# 1
Generar el código para que un usuario ingrese por teclado N
cantidad de números de tipo int el sistema debe validar cual
los números es el mayor y el menor(usar condicionales y ciclos)
"""

numeros=[];
numMayor=-99999
numMenor = 9999999
n = int(input("Ingresa cantidad de numeros"))
for i in range(n):
    numero=(int(input(f'Ingresa numero {(i+1)}')));
    if numero < numMenor:
        numMenor = numero
    elif numero> numMayor:
        numMayor = numero


print(f'SALIDA:\n numero menor es: {numMenor}\n numero mayor es: {numMayor}')

"""
#2
Declare una lista llamada con el nombre de temperatura, esta lista debe recibir la temperatura de 
diferentes ciudades en usuario debe ingresar por teclado el número total de temperaturas que desea ingresar y 
las diferentes temperaturas el algoritmo debe mostrar el promedio de la temperatura 
(aproximado a 1 decimal, y cuantos temperaturas son mayores que el promedio)
"""

temperatura=[]
sum=0;
count=0
m= int(input("Ingrese cantidad de temperatura"))
for i in range(m):
    temperatura.append(int(input(f'Ingresa temperatura de la ciudad  {(i+1)}:')));

for tem in temperatura:
    sum=sum+tem

promedio = sum/m

for temSum in temperatura:
    if temSum >= promedio:
        count=count+1

print(f'\nSALIDA:Promedio Temperaturas {promedio}\nTemperaturas >= al promedio {count}')

""""
#3
Realice la codificación que permita guardar un dato string (password) en una variable, y posterior a esto realice la petición 
por consola para que ingrese una contraseña, luego debe validar y mostrar por consola si el password ingresado por consola es 
el igual al almacenado en la variable.
"""

password = "hola1234";
passUser = input("ingresa la clave")
if password==passUser:
    print("Clave correcta")
else:
    print("Clave incorrecta")

"""
#4
Realice la codificación que solicite a una persona el peso en KG también que pida la estatura mts, 
con estos datos se debe realizar el cálculo de IMC (índice de masa corporal) guardarlo en una variable, 
y luego mostrarlo por consola de la siguiente manera (`Tu índice de masa corporal es ) donde `` 
es el índice de masa corporal calculado redondeado con dos decimales.
"""

masa= float(input("Ingresa el peso en KG"))
altura= float(input("Ingresa la estatura en MTS ejem: 1.75"))

imc = masa/(altura**2)
print(f'Tu Indice de masa corporal es {round(imc,2)}')

""""
#5
-	complete el código para que la función retorne el parámetro X+5 llene las casillas en blanco con el código faltante def mi_funcion(x): 
-	se pide imprima el primer parámetro para esto llene la casilla en blanco faltante
"""

def mi_funcion(x):
    return x+5

    def funcion(nombre,apellido):
        print(nombre)

"""
#6 
Realice un algoritmo que solicite un password ingresándolo por consola y la vuelva a solicitar para confirmarla hasta 
que las dos contraseñas coincidan no se salga del ciclo """
count = 1;
while count!=0:

    password1 = input("Digita la contraseña")
    password2 = input("Confirma tu contraseña")

    if password1 == password2:
        print("Contraseña valida")
        count = 0;
    else:
        print("Contraseña invalida")

""" 
#7
Insert to the following dictionary Vehicle the key/value “Price”: 10000 (by using a python input function)"""
vehicle = {
 "brand": "Chevrollet",
 "model": "Camaro",
 "year": 2000,
 "condition":"Second hand"
}
value = input("Ingrese el value")
key = input("Ingrese el key")

vehicle[key] = value
print(vehicle)
