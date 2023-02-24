""""
Ejercicio : Validad estación del año según el mes

## Variables

dia = input("Ingresa día");
mes =int (input("Ingresa mes"));
año = input("Ingresa año");
fecha = "";


## Validación
if mes >=1 and mes <=2 or mes ==12 :
    print(f'Estación del año: INVIERNO. Fecha {dia}/{mes}/{año}');
elif mes >=4 and mes <=6:
    print(f'Estación del año: PRIMAVERA Fecha {dia}/{mes}/{año}');
elif mes >=7 and mes <=9:
    print(f'Estación del año: VERANO Fecha {dia}/{mes}/{año}');
elif mes ==10 or mes == 11:
    print(f'Estación del año: OTOÑO Fecha {dia}/{mes}/{año}');
else: print("Mes no existente");

"""
## Variable
nota =int (input("Ingresa tu notta (entre 0 y 10)"));
calificacion = "";

if nota >=9 and nota <= 10:
    calificacion = "A"
elif nota >=8 and nota<9:
    calificacion = "B"
elif nota>=7 and nota<8:
    calificacion = "C"
elif nota>=6 and nota <5:
    calificacion = "D"
elif nota >= 0 and nota <=6:
    calificacion = "F";

else: calificacion = "NOTA DESCONOCIDA"

print(f'SU CALIFICACIÓN ES...{calificacion}')