def calcular_temperatura_promedio(datos):
    # Inicializamos un diccionario para almacenar las temperaturas por ciudad
    temperaturas_por_ciudad = {}

    # Recorremos los datos proporcionados
    for ciudad, semanas in datos.items():
        # Inicializamos una lista para almacenar las temperaturas por semana
        temperaturas_por_semana = []

        # Recorremos las semanas de cada ciudad
        for semana, temperaturas in semanas.items():
            # Calculamos la temperatura promedio de la semana y la agregamos a la lista
            promedio_semana = sum(temperaturas) / len(temperaturas)
            temperaturas_por_semana.append(promedio_semana)

        # Calculamos la temperatura promedio de la ciudad y la almacenamos en el diccionario
        promedio_ciudad = sum(temperaturas_por_semana) / len(temperaturas_por_semana)
        temperaturas_por_ciudad[ciudad] = promedio_ciudad

    return temperaturas_por_ciudad


# Ejemplo de datos de temperaturas por ciudad y semana
datos_temperaturas = {
    'PUTUMAYO': {
        'Semana 1': [25, 28, 26, 24, 27],
        'Semana 2': [23, 22, 24, 25, 21]
    },
    'QUITO': {
        'Semana 1': [30, 32, 31, 29, 28],
        'Semana 2': [27, 26, 28, 29, 30]
    }
}

# Llamamos a la función con los datos proporcionados
resultados = calcular_temperatura_promedio(datos_temperaturas)

# Imprimimos los resultados
for ciudad, temperatura_promedio in resultados.items():
    print(f"La temperatura promedio en {ciudad} es: {temperatura_promedio}")