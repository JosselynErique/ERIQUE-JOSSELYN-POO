# Creación de un diccionario simple
persona = {
    "nombre": "JOSSELYN",
    "edad": 29,
    "ciudad": "JOYA DE LOS SACHAS"
}

# Acceso a un valor
print(persona["nombre"])  # Salida: JOSSELYN

# Modificación de un valor
persona["edad"] = 29

# Agregar un nuevo par clave-valor
persona["ocupacion"] = "Ingeniera"
print(f'Ocupación agregada: {persona["ocupacion"]}')

# Eliminación de un par clave-valor
# Elimina el par clave-valor con la clave "ciudad"
del persona["ciudad"]
print("Clave 'ciudad' eliminada.")

# Uso de .items() para iterar sobre el diccionario
print("\nInformación de la persona:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
