#Practicando github en línea
# print(Cabeza dura no entiendes)
#print(Resetea tu cerebro)
#print(Cabeza hueca se te olvido setear el guardado automático)
#RECUERDA ESTE ORDEN: 
# 1.- MODIFICAR EL CÓDIGO   2.- GIT ADD .  3.- GIT COMMIT -M "COMENTARIO DENTRO"   4.- GIT PUSH PARA GUARDAR EN LÍNEA

# 1. Control de asistencia
# asistencia = ["Ana", "Carlos", "Elena", "Tomás"] 
# a) Agregue un nuevo estudiante ingresado por teclado al final de la lista. 
# b) Muestre cuántos estudiantes asistieron. 
# c) Ordene alfabéticamente la lista y la muestre.

# asistencia = ["Ana", "Carlos", "Elena", "Tomás", "Rodrigo"]
# print(len(asistencia))
# asistencia.sort()
# print(asistencia)

# 2. Inventario de una tienda
# stock = [15, 8, 23, 12, 5] 
# a) Muestre el stock total. 
# b) Indique cuál es el producto con mayor stock y cuál con menor stock. 
# c) Agregue un nuevo valor de stock ingresado por teclado.

# stock = [15, 8, 23, 12, 5, 25]
# suma = sum(stock)
# print(suma)
# maximo = max(stock)
# print(maximo)
# minimo = min(stock)
# print(minimo)

# 3. Lista de espera de una consulta médica
# pacientes = ["María", "Pedro", "Sofía", "Luis"] 
# a) Muestre el primer paciente atendido (elimínelo de la lista). 
# b) Agregue un paciente urgente en la primera posición. 
# c) Muestre la lista actualizada.

# pacientes = ["María", "Pedro", "Sofía", "Luis"]
# print(pacientes[0])
# pacientes.remove("María")
# print(pacientes)
# pacientes.insert(0, "Rodrigo")
# print(pacientes)

# 4. Notas de una evaluación
# notas = [5.4, 6.2, 4.8, 5.9, 3.7]
# a) Muestre la nota más alta y la más baja.
# b) Calcule la suma de todas las notas.
# c) Muestre las notas ordenadas de menor a mayor sin modificar la lista
# original.

# notas = [5.4, 6.2, 4.8, 5.9, 3.7]
# maximo=max(notas)
# minimo=min(notas)
# suma=sum(notas)
# notas.sort()
# print(f"La nota más alta fue: {maximo} y la más baja {minimo}")
# print(f"La suma de toda las notas es: {suma} y si las ordenamos de menor a mayor se verían así:{notas}")

# 5. Carrito de compras
# precios = [2500, 1800, 3200, 1500]
# a) Agregue un nuevo precio ingresado por teclado.
# b) Elimine el último producto agregado.
# c) Muestre el total de la compra y la cantidad de productos.

# precios = [2500, 1800, 3200, 1500]
# print(f"Lista inicial: {precios}")
# precios = [2500, 1800, 3200, 1500, 22000]
# print(f"\nLista con nuevo precio agregado por teclado: {precios}")
# precios.remove(22000)
# print(f"\nEliminando el úlimo producto agregado: {precios}")
# suma=sum(precios)
# cantidad=len(precios)
# print(f"\nEl total de la compra fue: {suma} y la cantidad de productos: {cantidad}")

# 6. Ranking de puntajes
# puntajes = [1200, 850, 2300, 1750, 980]
# a) Ordene los puntajes de mayor a menor.
# b) Muestre el puntaje máximo y el mínimo.
# c) Indique cuántos puntajes hay registrados.

# puntajes = [1200, 850, 2300, 1750, 980]
# puntajes.sort()
# puntajes.reverse()
# maximo=max(puntajes)
# minimo=min(puntajes)
# cantidad=len(puntajes)
# print(f"Puntajes ordenados de mayor a menor: {puntajes}")
# print(f"El puntaje máximo fue: {maximo} y el mínimo: {minimo}")
# print(f"Se registraron {cantidad} puntajes.")

# 7. Biblioteca escolar
# libros = ["El Principito", "1984", "Drácula", "Harry Potter"]
# a) Agregue un nuevo libro al final.
# b) Elimine un libro cuyo nombre sea ingresado por teclado.
# c) Muestre la lista ordenada alfabéticamente.

# libros = ["El Principito", "1984", "Drácula", "Harry Potter"]
# print(f"Lista inicial: {libros}")
# libros.append("Dragon Ball Super")
# print(f"\nLista con nuevo libro al final: {libros}")
# libro_a_eliminar = input("\nIngrese el nombre del libro a eliminar: ")
# libros.remove(libro_a_eliminar)
# print(f"\nLista con libro eliminado: {libros}") 
# libros.sort()
# print(f"\nLibros ordenados alfabeticamente: {libros}")

#8. Registro de temperaturas 
#temperaturas = [18, 20, 17, 22, 19, 21, 16] 
#a) Muestre la temperatura más alta y la más baja. 
#b) Calcule la suma de todas las temperaturas. 
#c) Indique cuántos días fueron registrados.

# temperaturas = [18, 20, 17, 22, 19, 21, 16]
# maximo=max(temperaturas)
# minimo=min(temperaturas)
# suma=sum(temperaturas)
# cont=len(temperaturas)
# print(f"La temperatura más alta fue de {maximo}°C, la más baja {minimo}°C.")
# print(f"Suman un total de: {suma}°C y se registraron durante {cont} días.")

#9. Cola de atención en un banco 
#clientes = ["José", "Patricia", "Camila", "Felipe"] 
#a) Atienda al primer cliente (elimínelo de la lista). 
#b) Agregue un nuevo cliente al final. 
#c) Muestre la cantidad de clientes que quedan esperando.

# clientes = ["José", "Patricia", "Camila", "Felipe"]
# print(f"Lista inicial de clientes: {clientes}")
# clientes.remove("José")
# print(f"\n¡Primer cliente atendido!, esperando su turno: {clientes}")
# clientes.append("Rodrigo")
# print(f"\n¡Nuevo cliente ingresado a la lista!: {clientes}")
# cont=len(clientes)
# print(f"\nAún por atender: {cont} clientes")

#10. Gastos mensuales 
#gastos = [12000, 8500, 23000, 15000, 9800] 
#a) Muestre el gasto total del período. 
#b) Indique el gasto mayor y el menor. 
#c) Agregue un nuevo gasto ingresado por teclado. 
#d) Muestre los gastos ordenados de menor a mayor. 

# gastos = [12000, 8500, 23000, 15000, 9800]
# print(f"Lista de gastos: {gastos}")
# suma=sum(gastos)
# print(f"\nEl gasto total del periodo es de: {suma} pesos.")
# maximo=max(gastos)
# minimo=min(gastos)
# print(f"\nEl mayor gasto fue {maximo} y el menor {minimo} pesos.")
# nuevo_gasto=int(input("\nIngrese un nuego gasto: "))
# gastos.append(nuevo_gasto)
# print(f"\nNuevo gasto agregado a la lista: {gastos}")
# gastos.sort()
# print(f"\nGastos ordenados de menor a mayor: {gastos}")

               #Desafío Integrador: Administración de un cine
               
#ventas = [120, 95, 150, 80, 110] 
#Construya un programa que permita realizar las siguientes acciones: 
#1. Agregar las ventas de un nuevo día. 
#2. Eliminar el último día registrado. 
#3. Mostrar la cantidad de días registrados. 
#4. Mostrar el total de entradas vendidas. 
#5. Mostrar el día con mayor y menor cantidad de ventas. 
#6. Mostrar una copia de las ventas ordenadas de menor a mayor. 
#7. Finalmente, ordenar la lista original y mostrarla.

# ventas = [120, 95, 150, 80, 110]
# print(f"Listado de ventas: {ventas}")
# ventas2 = [80, 55, 190, 90, 100]
# ventas.extend(ventas2)
# print(f"\nVentas nuevo día agregadas: {ventas}")
# ventas.pop()
# ventas.pop()
# ventas.pop()
# ventas.pop()
# ventas.pop()
# print(f"\nVentas último día eliminadas (volvemos al original): {ventas}")
# cant=len(ventas)
# print(f"\nLos días registrados fueron: {cant}")
# suma=sum(ventas)
# print(f"\nEl total de entradas vendidas es: {suma}")
# maximo=max(ventas)
# minimo=min(ventas)
# print(f"\nEl día con mayor cantidad de ventas fue: {maximo} y el de menor: {minimo}")
# ventas.sort()
# print(f"\nCopia de ventas ordenada de menor a mayor: {ventas}")
# print(f"\nFinalmente, lista original ordenada: {ventas}")