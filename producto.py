class Producto:
  def __init__(self, nombre, cantidad, precio):
    self.nombre = nombre
    self.cantidad = cantidad
    self.precio = precio

  def agregar_unidades(self, unidades):
    self.cantidad += unidades

  def quitar_unidades(self, unidades):
    if unidades <= self.cantidad:
        self.cantidad -= unidades
    else:
        print("No hay suficientes unidades para quitar.")

  def calcular_valor_total(self):
    return self.cantidad * self.precio