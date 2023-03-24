#Importar
import  tkinter as tk
import tkinter as ttk
from tkinter import ttk,messagebox

# ventana tk

ventana = tk.Tk()

# tamaño de la ventana
ventana.geometry('430x430')

#4. Cambiar nombre de la ventana
ventana.title("Convertidor de grados 15%")
ventana.columnconfigure(0,weight=0)


#  --- FUNCIONES ---

# crear variable para almacenar respuestas
respuestas = ""
texto = ""
concateRtaText = ""

# funcion de celsius a fahrenheit
def celsius_fahrenheit():
    global respuestas,texto,concateRtaText

    # obtener texto y convertir a int
    formula = ((float(entrada1.get()) * 9 / 5) + 32)

    # concatenar respuesta a variable
    respuestas += str(formula) + "\n"
    texto += "Conversion a Fahrenheit" + "\n"
    concateRtaText+="Grados celsius ingresado: "+entrada1.get()+ "\n   El equivalente en grados F°: "+str(formula)+"\n"


    # mostrar resultado concatenado
    labelFormula = ttk.Label(ventana, text=respuestas)
    labelFormula.grid(row=4, column=2, columnspan=2)

    # mostrar texto
    labelTexto = ttk.Label(ventana, text=texto)
    labelTexto.grid(row=4, column=0,columnspan = 2)


# funcion de fahrenheit a celsius
def fahrenheit_celsius():
    global respuestas,concateRtaText
    global  texto

    # obtener texto, convertir a int y redondear
    formulaC = ((float(entrada1.get())-32)*5/9).__round__(1)

    # concatenar respuesta a variable
    respuestas += str(formulaC)+"\n"
    texto += "Conversion a Celcius"+"\n"
    concateRtaText += "Grados Fahrenheit ingresado: " + entrada1.get() + "\n    El equivalente en grados C°: " + str(formulaC) + "\n"


    # mostrar resultado
    labelFormula = ttk.Label(ventana, text=respuestas)
    labelFormula.grid(row=4, column=2, columnspan=2)

    # mostrar texto
    labelTexto = ttk.Label(ventana, text=texto)
    labelTexto.grid(row=4, column=0, columnspan=2)


def exportararchivo():
    global concateRtaText
    try:
        archivo = open("E:/Semestre V/Tendencias en Desarrollo de Software/convertidor_grados.txt", "w")
        archivo.write(concateRtaText)
    except Exception as e:
        print(e)
    finally:
        archivo.close()
        messagebox.showinfo("Mensaje informativo ","Datos exportados :)")




#label titulo
label_titulo= ttk.Label(ventana,text="Convertidor de grados 15%",padding=15)
label_titulo.grid(row=0,column=2)

#entrada valor
entrada1 = ttk.Entry(ventana,width=30)
entrada1.grid(row=1,column=2,padx=20,pady=20)

#boton convertir a farenheit
botonF=ttk.Button(ventana,text = "Convertir a Fahrenheit",command=celsius_fahrenheit)
botonF.grid(row=2,column=1);

#boton convertir a celsius
botonC=ttk.Button(ventana,text = "Convertir a Celsius",command=fahrenheit_celsius)
botonC.grid(row=2,column=2);

#boton exportar
botonExp=ttk.Button(ventana,text = "Exportar",command=exportararchivo)
botonExp.grid(row=2,column=3);
ventana.mainloop();
