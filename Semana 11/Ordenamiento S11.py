

matriz = [
    [4, 5, 3],
    [8, 2, 7],
    [9, 0, 8]
]

def bubble_sort_fila (fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def ordenar_fila_matriz(matriz, fila):

if fila < 0 or fila >= len(matriz):
#fila específica
    bubble_sort(matriz[fila])
for fila in matriz:
        print(fila)
    print()

    print("Matriz Original:")
    imprimir_matriz(matriz)

    fila_a_ordenar = 1
    matriz_ordenada = ordenar_fila_matriz(matriz, fila_ordenar)
    print(f"Matriz con la fila {fila_a_ordenar} ordenada:")
    imprimir_matriz(matriz_ordenada)


