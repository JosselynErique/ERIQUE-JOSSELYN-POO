# Creación de una lista
frutas = ["mandarina", "uva", "fresas"]

# Añadir un elemento
frutas.append("naranja")  # Añade "naranja" al final de la lista
# `pop` solo debe usar un índice válido. Se eliminó el segundo argumento incorrecto
# frutas.pop(1, "banano")  # Esto es incorrecto y se debe eliminar

# Acceder a un elemento
print(frutas[0])  # Imprime "mandarina"
print(frutas[1])  # Imprime "uva"

# Eliminar un elemento
frutas.remove("uva")  # Elimina "uva" por nombre
frutas.pop(1)  # Elimina el elemento en el índice 1, que es "fresas"

# Imprimir la lista modificada
print(frutas)  # Imprime ['mandarina', 'naranja']
