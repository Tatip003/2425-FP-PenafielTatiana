# Búsqueda en Arreglo Multidimensional
matriz = [
    [30, 10, 15]
  o  [25, 35, 5]
    [40, 20, 45]
]
# Busqueda de valor especifico
valor_buscado = 5

fila_encontrada = -1
columna_encontrada =-1

#Recorrer
for fila in range(len(matriz)):
     for columna in range (len(matriz[fila])):
         if matriz [fila] [columna] == valor_buscado:
             fila_encontrada = fila
             columna_encontrada = columna

              break
        if fila_encontrada != -1:
               break

# Busqueda valor especifico 3n la matriz
if fila_encontrada != -1:
    printf(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}" )
else :
    Printf(f"{valor_buscado} no se encontró en la matriz" )