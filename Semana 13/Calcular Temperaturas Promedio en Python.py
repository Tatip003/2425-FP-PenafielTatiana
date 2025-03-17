#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
# #primera dimensión : (Quito, Manta y Cuenca
# otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.)
# La tercera dimensión, semanas.

temperatura = [
    {"ciudad": "Guayaquil", "semanas": [

        [   # Semana 1
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 31}
        ]
    ]},
        {"ciudad": "Manta", "semanas": [
         [ # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 39}
        ],
           [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 31}
          ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 39},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 30}
        ]
    ]},
    {"ciudad": "Cuenca", "semanas": [
        [# Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 20}
        ]
     ]}
]
#calcule la temperatura promedio de una ciudad durante un período de tiempo
def promedio_de_temperatura_de_ciudad(temperaturas):
    """
    Calcular la temperatura promedio de cada ciudad durante un período de tiempo dado.

    :param temperaturas: lista de diccionarios con los datos de las temperaturas
    :return: Diccionario con las ciudades y temperaturas promedios
    """
    promedios = {}
    for ciudad in temperaturas:
        total_temperatura = 0
        total_dias = 0

        for semana in ciudad["semanas"]:
            for dia in semana:
                total_temperatura += dia["temp"]  # Corregido "temperatura" a "temp"
                total_dias += 1

        promedio_ciudad = total_temperatura / total_dias
        promedios[ciudad["ciudad"]] = round(promedio_ciudad, 2)  # Redondeamos a 2 decimales


    return promedios


# Llamar a la función
resultados = promedio_de_temperatura_de_ciudad(temperatura)

print("\nPromedio de temperaturas por cada ciudad:")
for ciudad, promedio in resultados.items():
    print(f'{ciudad}: {promedio}°C')  # Mostrar las temperaturas en grados Celsius