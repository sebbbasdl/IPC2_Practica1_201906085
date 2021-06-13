from graphviz import Source

class Nodo(object):
    def __init__(self,nombre=None, apellido=None, telefono=None, siguiente=None, anterior=None):
        self.telefono = telefono
        self.nombre = nombre
        self.apellido = apellido
        self.siguiente = siguiente
        self.anterior= anterior

    def __str__(self):
        return "%s,%s,%s" % (self.nombre, self.apellido, self.telefono)

class Lista(object):
    def __init__(self):
        self.contador=0
        self.cola = None
        self.cabe=None



    def insertar(self, dato):
        nodo=Nodo(dato)

        if self.cabe is None:
            self.cabe=nodo
            self.cola=self.cabe
        else:
            nodo.anterior=self.cola
            self.cola.siguiente=nodo
            self.cola=nodo

        self.contador += 1

    def ordenar(self):
        actual=self.cabe

        while actual:
            dato = actual.dato
            actual=actual.siguiente
            yield dato

    def listar(self):
        temp=self.cabe
        while temp!=None:
            print(temp)
            temp=temp.siguiente



lista=Lista()



menup = """
Menu
1. Ingresar nuevo contacto
2. Buscar contacto
3. Visualizar agenda
4. Salir
"""

listaV=[]
var=True
contX=0
contY=3
while var == True:
    print(menup)
    opcion =int(input("Escoja una opcion:  "))
    if opcion == 1:
        nombre=(input("Ingrese el nombre:"))
        apellido = (input("Ingrese el apellido:"))
        numero = (input("Ingrese el numero:"))

        nodo1=Nodo(nombre,apellido,numero)

        lista.insertar(nodo1)
        bar = str(nodo1)
        listaTemp=[]
        listaTemp.extend((bar.split(",")))
        listaV.append(listaTemp)
        contX+=1


        print(listaTemp)
        print(listaV)





    elif opcion ==2:
        numero1 = (input("Ingrese el numero:"))

        for x in range(contX):
            for y in range(contY):

                valor =(listaV[x][y])

                if valor==str(numero1):
                    nom=str(listaV[x][y-2])
                    ape=str(listaV[x][y-1])

                    print("Valor encontrado:\n"+"Nombre: "+nom+", Apellido: "+ape+", Telefono:"+valor)
                elif x==contX-1 and y==contY-1:
                    op=(input("Contacto no existe, desea agregarlo(responder: SI o NO): "))

                    if str(op) == "SI":
                        nombre = (input("Ingrese el nombre:"))
                        apellido = (input("Ingrese el apellido:"))


                        nodo1 = Nodo(nombre, apellido, numero1)

                        lista.insertar(nodo1)
                        bar = str(nodo1)
                        listaTemp = []
                        listaTemp.extend((bar.split(",")))
                        contY += 3
                        listaV.append(listaTemp)
                        contX += 1
                    else:
                        var=True


    elif opcion==3:
        print(listaV)
        listaC=[]
        tempG="digraph L{\n\n\tnode [shape=record fontname=Arial];\n\n\t"
        contador1=0
        for nueva in listaV:
            nombre1=nueva[0]
            apellido1=nueva[1]
            telefono1=nueva[2]
            contador1 +=1
            listaC.append("a"+str(contador1))

            tempG+="a"+str(contador1)+"[label=\"Nombre: "+nombre1+"\lApellido:"+apellido1+"\lTelefono: "+telefono1+"\l\"]\n\n\t"
        fin = len(listaC)
        contador2=0
        for name in listaC:
            contador2+=1
            print("contador2:"+str(contador2))

            if contador2==fin:
                tempG+=name
            else:
                tempG+= name+"->"
        tempG+="\n\n}"

        print(listaC)

        print(fin)
        print("Visualizar")
        #tempG = "digraph L{\n\n\tnode [shape=record fontname=Arial];\n\n\ta"+contador1+"[label=\"Nombre: "+nombre+"\lApellido:"+apellido+"\lTelefono: "+telefono+"\l\"]\n\n\tb  [label=\"one\ltwo three\lfour five six seven\l\"]\n\n\ta -> b\n\n}"


        print(tempG)
        s = Source(tempG, filename="agenda", format="png")
        s.view()

    elif opcion==4:
        print("Se ha cerrado el programa")
        var=False

    else:
        print("No ha ingresado una opcion valida")


