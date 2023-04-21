# ----LISTAS----

nombres =['Luis','Lina','Laura','Jhon'];

## imprimir posicion en especifico

print(f'{nombres[1:]}');
## [0:2]=Obtener rango entre 0 y 2, e imprime los dos anteriores = ['Luis', 'Lina']
## [:3]=Obtener los 3 primeros = ['Luis', 'Lina', 'Laura']
## [1:]=Obtener desde esa posicion en adelante = ['Lina', 'Laura', 'Jhon']

# --Realizar cambio en una lista--
nombres[3]="Sandra";
print(nombres) ## ['Luis', 'Lina', 'Laura', 'Sandra']


# -- Iterar nombres en la lista --
for nombre in nombres:
    print(nombre)
    """"
    Luis
    Lina
    Laura
    Sandra
    No existen mas nombres en la lista
    """
else:
    print('No existen mas nombres en la lista')

# -- Obtener cantidad elementos tiene la lista --

print(len(nombres)) # 4

# --  Anexar elemento --
nombres.append('Lorenzo')
print(nombres) # ['Luis', 'Lina', 'Laura', 'Sandra', 'Lorenzo']

# -- Anexar elemento en posicion especifica
nombres.insert(1,'Vanessa');
print(nombres) # ['Luis', 'Vanessa', 'Lina', 'Laura', 'Sandra', 'Lorenzo']

# -- Eliminar ultimo elemento --
nombres.pop();
print(nombres); # ['Luis', 'Vanessa', 'Lina', 'Laura', 'Sandra']

# --  Eliminar elemento en especifico --
del nombres[0];
print(nombres); # ['Vanessa', 'Lina', 'Laura', 'Sandra']

# Eliminar todos elementos de la lista
nombres.clear();
print(nombres); # []

#--------------------------------------------------------------------------------#
"""""
Ejercicio #1
listaMaterias = [];

## Ingresar cantidad materias
n= int(input("Ingresa numero materias:"));

# Ingresar cada una de las materias
for i in range(n):
    listaMaterias.append(input(f'Ingresa materia #{(i+1)}'));

# mostrar cada una de las materias
for materia in listaMaterias:
    print(f'Yo estudio {materia.upper()}');
else:
    print("-----")
"""

numerosGanadores=[];

# Ingresar 6 numeros
for i in range(6):
    numerosGanadores.append(int(input(f'Ingresa numero {(i+1)}')));

## ordena lista
numerosGanadores.sort() # [1, 3, 4, 4, 6, 7]
print(numerosGanadores)
# imprimir lista
for num in numerosGanadores:
    print(f'Numeros ganadores:{num}')
else:
    print("-------")

# ********Tuplas********

# Definir una tupla
frutas =('Naranja','Mango','Fresa');
print(frutas); #('Naranja', 'Mango', 'Fresa')

#numero total de elementos
print(len(frutas)); #3

#acceder a un elemento
print(frutas[0]); # Naranja


#acceder ultimo elemento
print(frutas[-1]); #Fresa

#acceder a un rango
print(frutas[0:1]); #('Naranja')

# ************************

# ********Set de datos********

planetas = {'Marte','Jupiter','Venus'}
print(planetas)

# largo del set
print(len(planetas)); # {'Marte', 'Jupiter', 'Venus'}

# Validar si hay un elementos
print('Marte' in planetas); # True

# agregar un elemento
planetas.add('Tierra'); # {'Marte', 'Tierra', 'Jupiter', 'Venus'}
print(planetas)
#********************************

# ********Diccionario********
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Objected Oriented Programming',
    'DBMS' : 'Database Management System'
}
print(diccionario); # {'IDE': 'Integrated Development Environment', 'OOP': 'Objected Oriented Programming', 'DBMS': 'Database Management System'}

#cantidad de elementos
print(len(diccionario)); #3

#Acceder a un elemento del diccionario
print(diccionario['IDE']); # Integrated Development Environment

#Otra forma de recuperar un elemento
print(diccionario.get('OOP')); # Objected Oriented Programming

#Modificar elementos
diccionario['IDE']= 'Ambiente de Desarrollo Integrado'
print(diccionario); # {'IDE': 'Ambiente de Desarrollo Integrado', 'OOP': 'Objected Oriented Programming', 'DBMS': 'Database Management System'}


#********************************

#Funciones
def suma (a,b):
    return a+b

print(f'Resultado de la suma {suma(5,6)}'); #Resultado de la suma 11

# *: reciba varios valores

def listarNombres (*nombres):
    for nombre in nombres:
        print(nombre)
    else:
        print()
listarNombres('Juan','Pedro','Camila')

# Mostrar bienvenida
def saludo (nombre):
    return (f'Bienvenido {nombre} a la clase de nuevas tendencias :)');

print(saludo("LUCHO")) # Bienvenido LUCHO a la clase de nuevas tendencias :)

def sumaNumeros (*numeros):
    total=0;
    for suma in numeros:
        total=total+suma
    return total

print(sumaNumeros(5,5,5,5)) # 20

def imprimirNumeros(num):

    if num>1:
        print(num)
        imprimirNumeros(num-1)


imprimirNumeros(9)