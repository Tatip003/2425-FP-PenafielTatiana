

Información_personal = {
    "nombre": "Sophia",
    "edad": 35,
    "ciudad": "Bogota",
    "Profesion": "Ingeniera"}
print("Diccionario original:", Información_personal)

#Accede y modifica la clave ciudad
Información_personal["ciudad"] = "Quito"

#Agrega una nueva clave-valor  que represente la "profesion" de la persona
Información_personal["Profesion"] ="Abogada"


#añadir la clave 'telefono' y valor
Información_personal["telefono"] ="099-563-5636"

# Eliminar un elemento
del Información_personal["edad"]

# Imprimir el diccionario final
print("Información_personal")
print(" 'telefono':", Información_personal)