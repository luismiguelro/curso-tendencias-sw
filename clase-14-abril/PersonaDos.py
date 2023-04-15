class PersonaDos:
    def __init__(self,nombre,apellido,edad):
        #crear atributos y parámetros
        self.nombre=nombre
        self.apellido=apellido
        self.edad = edad

    # mostra detalle
    def mostrar_detalle(self):
        print(f'{self.nombre} {self.edad}')  # LuisMi 88




# tipo clase
print(type(PersonaDos)) #<class 'type'>

#Crear objetos
p1=PersonaDos('LuisMi','Rguez','88')

#imprimir
print(p1.nombre,p1.apellido,p1.edad) # LuisMi Rguez 88
p1.mostrar_detalle()

