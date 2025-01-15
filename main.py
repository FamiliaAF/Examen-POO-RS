from calculadora import Calculadora
from cine import TicketCine
from persona import Persona, Estudiante
from producto import Producto

calc = Calculadora()

print(calc.sumar(5, 3))
print(calc.restar(10,4))
print(calc.multiplicar(6, 7))
print(calc.dividir(8, 2))

ticket = TicketCine('Inception', '18:00', 'F5')
ticket.mostrar_detalles()
ticket.cambiar_asiento("G10")
ticket.mostrar_detalles()

persona = Persona("Carlos", 30)
persona.saludar()
estudiante = Estudiante('Pablo', 20, "Ingeniería")
estudiante.saludar()

producto = Producto("Laptop", 10, 1500)
producto.agregar_unidades(5)  
producto.quitar_unidades(3)  
print(producto.calcular_valor_total()) 