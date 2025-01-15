class TicketCine:
  def __init__(self, pelicula, horario, asiento):
    self.pelicula = pelicula
    self.horario = horario
    self.asiento = asiento

  def mostrar_detalles(self):
    print(f"Pelicula:{self.pelicula}, Horario:{self.horario}, Asiento:{self.asiento}.")

  def cambiar_asiento(self, nuevo_asiento):
    self.asiento = nuevo_asiento

  def cambiar_horario(self, nuevo_horario):
    self.horario = nuevo_horario  
  