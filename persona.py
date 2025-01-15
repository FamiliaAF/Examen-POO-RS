class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def saludar(self):
    print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
  def __init__(self, nombre, edad, carrera):
    super().__init__(nombre, edad)
    self.carrera = carrera

  def estudiar(self):
    print(f"Estoy estudiando {self.carrera}")

  def saludar(self):
    super().saludar()
    print(f"estoy estudiando {self.carrera}")