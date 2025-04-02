# Abrir archivo para escritura
Archivo = open('my_notes.txt', 'w')
# Escribir 3 líneas
Archivo.write('Es la primera semana de abril y oficialmente empezamos la ultima semana de clases.\n')
Archivo.write('Se avecina la semana de examenes y me siento muy nerviosa.\n')
Archivo.write('AL inicio del semestre veia tan lejos esta fecha, pero han pasado muy rapido.\n')
# Cerrar el archivo después de escribir
Archivo.close()

# Abrir archivo para lectura
Archivo = open('my_notes.txt', 'r')
# Indicar que se lee línea a línea y eliminar saltos de línea extras
print(Archivo.readline().strip())
print(Archivo.readline().strip())
print(Archivo.readline().strip())
# Cerrar el archivo
Archivo.close()
