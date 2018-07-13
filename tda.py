class Grafo:
  
  def __init__(self):
    self.vertices = {}
    self.cant_v = 0 #O(1)
    self.cant_e = 0 #O(1)
    
  def v(self):
    return self.cant

  def agregar_v(self, nombre, dato):
    
    if not nombre in self.vertices:
      v = Vertices(nombre, dato)
      self.vertice[nombre] = v
      self.cant_v += 1
  
class Vertice:
  
  """ constructor del vertice
      experimentando como distintos enfoques
  """
  def __init__(self, nombre, dato = None):
    self.lista_adyacencias = {} # para las conecciones
    self.nombre = nombre
    self.dato = dato #primero no dirigido (pruebas)
  
  def __str__(self):
    return str(self.nombre, self.dato)

