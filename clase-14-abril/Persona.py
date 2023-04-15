from PersonaDos import PersonaDos
# Crear clase
class Persona:
    #seria tipo constructor, self:this
    def __init__(self,name,age,telefono,*args,**kwargs):
        # atributos
        self.name=name
        self.age=age
        self.telefono= telefono

        # crear atributo
        self.args=args
        self.kwargs=kwargs

#declaración de objeto
p1= Persona("Luis",78,"34345",m="manazana",p="pera")
# p2= Persona("Miguel",66)

#Imprimir
print(p1.name,p1.age,p1.kwargs,p1.args)
# print(p2.name,p2.age)
obj = PersonaDos("juan","camilo","88")

obj.mostrar_detalle()