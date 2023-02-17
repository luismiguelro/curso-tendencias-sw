"""
print("Hola, mundo!");

myVariable="Hola, mundo desde Python!";
myVariable = 2;
print(myVariable);

#Asignar valor numerico a x
X=10;

#Asignar valor numerico a Y
Y=2;

#Valor de z que contiene X+Y
Z=X+Y;

print(X); #10
print(Y); #2

print("El valor de la variable Z es: ",Z); # El valor de la variable Z es:  12

# Obtener direccion en memoria de las variables
print("La variable X apunta a una dirección en la posición en memoria: ",id(X));
print("La variable Y apunta a una dirección en la posición en memoria: ",id(Y));
print("La variable Z apunta a una dirección en la posición en memoria: ",id(Z));

#IDENTIFICAR TIPO DE DATO

print(type("Hola!")) #<class 'str'>
print(type(20)) # <class 'int'>
print(type(20.0)) # <class 'float'>

V=True;
print(type(V)) # <class 'bool'>

# CONCATENAR
grupoFavorito = "Avenged Sevenfold "+ ",la mejor banda";

print("Mi grupo favorito es "+grupoFavorito); # Mi grupo favorito es Avenged Sevenfold ,la mejor banda
print(f'Mi grupo favorito es {grupoFavorito}');

#CONVERTIR VALORES CADENA A ENTEROS
numero1 = "1";
numero2 = "2";

print("Total:",(numero1+numero2));
print(f'Total: {int(numero1)+int(numero2)}');

# VALIDAR VARIABLES BOOLEAN
miVariable = False
print("--Ejercicio variables booleanas--");
# print(miVariable); # False
miVariable=2<1;
# print(miVariable) # True

# CONDICIONALES
if miVariable:
    print("Resultado verdadero");
else:
    print("Resultado falso");


## PROCESAR VALORES DE ENTRADA : input

resultado = int(input("Como estuvo tu día (1 al 10)...."));
print(f'Mi día estuvo: {resultado}/10')

# ACTIVIDAD

nombreLibro = input("Ingresa el título del ultimo libro que leiste");

infoAutor = input("Proporciona la inforamción del autor del libro");

print(f'*************************\n NOMBRE DEL LIBRO: {nombreLibro}\nAUTOR:{infoAutor}\n*************************');


# OPERADORES ARITMETICOS
operandoA=3;
operandoB=2;
suma=operandoA+operandoB;
resta=operandoA-operandoB;
multiplicacion=operandoA+operandoB;
division=operandoA/operandoB;
divisionEntero=operandoA//operandoB;
exponente=operandoA**operandoB;

print(f'****Resultados****'
      f'\nsuma: {suma}'
      f'\nResta: {resta}'
      f'\nMultiplicación: {multiplicacion}'
      f'\nDivisión: {division}'
      f'\nDivisión entero {divisionEntero}'
      f'\nExponente: {exponente}'
      f'\n*******************');


# AREA Y PERIMETRO DE UN RECTANGULO
alto = int(input("Ingresa el alto del rectangulo"));

ancho = int(input("Ingresa el ancho del rectangulo"));

area = alto*ancho;
perimetro=((alto+ancho)*2);

print(f'\n****AREA Y PERIMETRO****'
      f'\nÁREA: {area}'
      f'\nPERÍMETRO: {perimetro}'
      f'\n*******************');

# operadores de asignacion python

a=4;
b=2;
resultado = a!=b
print(f'Resultado == {resultado}')

# COMPARACIÓN
edad = int(input("Ingresa tu edad: "));

if edad>=18:
    print(f'Eres mayor de edad, tienes {edad}');
else:
    print(f'Eres menor de edad, tienes {edad} añitos :( ');


# OPERADORES AND / OR

valorMin = 10;
valorMax=20;

num = int(input("Ingresa un numero"));

if num >= valorMin and num <= valorMax:
    print(f'El valor {num} se encuentra dentro del rango')
else:
    print(f'El valor {num} NO se encuentra dentro del rango');
     """
# COVERSION NUMERO A TEXTO
num = int(input("Ingresa un numero entre 1 y 3"));
numeroTexto="";
if num == 1:
    numeroTexto = "Numero uno";
elif num == 2:
    numeroTexto = "Numero dos";
elif num == 3:
    numeroTexto = "Numero tres";
else: numeroTexto = "Valor fuera de rango"

print(f'Numero ingresado {num}, Numero en texto {numeroTexto}');




