class Grafo:
  
  def __init__(self):
    self.vertices = {}
    self.cant_v = 0
    self.cant_e = 0
    
  def v(self):
    return self.cant

  def agregar_v(self, nombre, dato):
    
    if not nombre in self.vertices:
      v = Vertices(nombre, dato)
      self.vertice[nombre] = v
      self.cant_v += 1
  
class Vertice:
  
  def __init__(self, nombre, dato):
    self.nombre = nombre
    self.dato = dato
  
  def __str__(self):
    return str(self.nombre, self.dato)

