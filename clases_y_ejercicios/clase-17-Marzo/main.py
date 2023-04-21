
# 1. Importar el módulo de tkinter para utilizarlo en el codigo
import  tkinter as tk
# 1.1 Importar tema para usar los componentes
import tkinter as ttk

#2. Objeto utilizando la clase tk
ventana = tk.Tk()

#3. Modificar tamaño de la ventana
ventana.geometry('600x400')

#4. Cambiar nombre de la ventana
ventana.title("Hola, Mundo!")

ventana.resizable()


# Configurar evento para usar un botón

#definir metodo evento
def evento1():
    #cambiar propiedad
    boton1.config(text='Botón 1 presionado...')

    #Crear nuevo boton
    #boton2 = ttk.Button(ventana,text="NUEVO BOTÓN")
    #boton2.grid(row=0,column=0)

def evento2():
    boton2.config(text='Botón 2 presionado...')


#5 crear el boton, objeto padre es la ventana
boton1=ttk.Button(ventana,text = "Dar click 2",command=evento1)


# Usar metodo grid
boton1.grid(row=0,column=0)

#boton1.pack()


ventana.columnconfigure(0,weight=0)
ventana.rowconfigure(0,weight=0)
#crear textbox
entrada1 = ttk.Entry(ventana,width=30)

# pintarlo en la grid
entrada1.grid(row=2,column=0)

def obtener_texto():
    texto = entrada1.get()
    label = ttk.Label(ventana,text=texto)
    label.grid(row=4, column=0,columnspan=2)
    entrada1.delete(0,tk.END)


    print(texto)

boton2=ttk.Button(ventana,text = "Obtener texto",command=obtener_texto)
boton2.grid(row=3,column=0)

#Manejo de mesagebox
from tkinter import ttk,messagebox

# Creacion mensaje informativo
Mensaje1 = "Datos actualizados"
#messagebox.showinfo("Mensaje informativo ",Mensaje1 + " informativo")
#messagebox.showerror("Mensaje error",Mensaje1 + " Error")

# importar la clase para usar objeto menu
from tkinter import ttk,Menu

# Crear función para el menú
def crea_menu():

    #configurar el menu ppal de la app
    menu_principal = Menu(ventana)

    #tearoff = False para evitar que no se separe el menu de la interfaz
    submenu_archivo = Menu(menu_principal,tearoff=0)

    #agregar una nueva opcion
    submenu_archivo.add_command(label='NUEVO..')
    submenu_archivo.add_command(label='NUEVO X2')

    # Agg submenu principal
    menu_principal.add_cascade(menu=submenu_archivo,label='Archivo')
    menu_principal.add_cascade(menu=submenu_archivo,label='Archivo 2')

    #mostrar menu en la ventana ppal
    ventana.config(menu=menu_principal)

# llamar a la funcion crear menu
crea_menu()
ventana.mainloop();