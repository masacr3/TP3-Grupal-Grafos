class Vertice:
    #constructor del vertice
    def __init__(self, clave, dato=None):
        self.ady = {} #adyacencias del vertice  clave: dato
        self.clave = clave
        self.dato = dato

    def __str__(self):
        return str(self.clave)

class Grafo:
    """Objeto Grafo G(V,E) donde V es la cantidad de vertices y E cantidad de Aristas """


    #constructor del grafo
    def __init__(self):
        self.vertices = {} #
        self.cantV = 0
        self.cantA = 0

    #retorna cantidad Vertices
    def cantidad_vertices(self):
        return self.cantV

    #retorna cantidad cantidad aristas
    def cantidad_aristas(self):
        return self.cantA

    #agrega vertice al grafo
    def agregar_vertice(self, clave, dato=None):
        if clave not in self.vertices:
            v = Vertice(clave ,dato)
            self.vertices[clave] = v
            self.cantV +=1
            return True
        return False

    #agrega arista al grafo
    def agregar_arista(self, a, b, dirigido=None ):
        if a == b or a not in self.vertices or b not in self.vertices :
            return False

        #obtengo los vertices
        verticeA = self.vertices[a]
        verticeB = self.vertices[b]

        if a not in verticeB.ady and b not in verticeA.ady:
            # a -> b
            verticeA.ady[b] = verticeB

            if not dirigido:
                # a <- b
                verticeB.ady[a] = verticeA

            self.cantA += 1
            return True

        return False

    #muestra las conecciones de los vertices en el grafo
    def ver_conecciones(self, clave):
        if clave in self.vertices:
            print("\n",clave,"\n │")
            for ady in self.vertices[clave].ady:
                print(" ├",ady)

    #borra vertice del grafo
    def borrar_vertice(self, clave):
        if clave not in self.vertices:
            return False

        for k in self.vertices[clave].ady:
            del self.vertices[k].ady[clave]
            self.cantA -= 1

        del self.vertices[clave]
        self.cantV -=1

        return True

    #posibles primitivas
    def obtener_vertices(self):
        return list(self.vertices)

    #si el vertice a es adyacente en b
    #para grafos no dirigidos
    def son_adyacentes(self, a, b):
        if a not in self.vertices and b not in self.vertices:
            return False

        if a in self.vertices[b].ady:
            return True

        return False



    #formalidad
    def __str__(self):
        lista = []
        #retorna clave
        for k in self.vertices:
            lista.append(k)
            lista.append( list( self.vertices[k].ady ) )

        return str(lista)


#La prueba de mierda
def prueba():
    g = Grafo()

    ok = True
    ok = ok and True == g.agregar_vertice("a")
    ok = ok and True == g.agregar_vertice("b")
    ok = ok and True == g.agregar_vertice("c")
    ok = ok and True == g.agregar_vertice("d")
    print("\t\t┌───────────────────────────────────┐")
    print("\t\t│                                   │")
    print("\t\t│~~~ TEST Grafos ~~~  by @Leonel R. │")
    print("\t\t│                                   │")
    print("\t\t│       Facultad de Ingenieria      │")
    print("\t\t│    Universidad de Buenos aires    │")
    print("\t\t│                                   │")
    print("\t\t└───────────────────────────────────┘")
    print("\n\n")
    print("agregar nodos ","...OK!" if ok else "...ERROR")

    print("conectar a-b es verdadero ", "...OK!" if g.agregar_arista("a","b") else "...ERROR")
    print("conectar a-a es falso ","...OK!" if not g.agregar_arista("a","b") == True else "...ERROR")
    print("conectar a-c es verdadero","...OK!" if g.agregar_arista("a","c") else "...ERROR")
    print("conectar a-d es verdadero","...OK!" if g.agregar_arista("a","d") else "...ERROR")
    print("conectar b-d es verdadero","...OK!" if g.agregar_arista("b","d") else "...ERROR")

    print("Cantidad vertice es igual 4 ","...OK!" if g.cantidad_vertices() == 4 else "...ERROR")
    print("Cantidad de aristas es igual a 4", "...OK!" if g.cantidad_aristas() == 4 else "...ERROR")

    #el g.vertices["b"]

    for v in g.vertices:
        g.ver_conecciones(v)

    print("\nborrar vertice [a] ", "...OK" if g.borrar_vertice("a") else "ERROR")
    print("Cantidad vertice es igual 3 ","...OK!" if g.cantidad_vertices() == 3 else "...ERROR")
    print("Cantidad aristas es igual 1 ","...OK!" if g.cantidad_aristas() == 1 else "...ERROR")
    for v in g.vertices:
        g.ver_conecciones(v)

prueba()

#TOMAAAAA SON LAS 9 de la mañana y sigo programando
#   _,,,,,,,__
# ((* )(* )   )
#  \  l     /           Marto Gato aprende a usar objetos
#   \  ¬  /
#    VVVV
