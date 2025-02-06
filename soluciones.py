# Primer ejercicio:

precios_usd = [10, 20, 35, 50, 100]
precios_eur = list(map(lambda x: round(x * 0.92, 2), precios_usd))
print(precios_eur)  


# Segundo ejercicio: 

edades = [12, 18, 25, 30, 15, 10, 21]
mayores_edad = list(filter(lambda x: x > 18, edades))
print(mayores_edad)  


# Tercer ejercicio:

personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Juan", "edad": 22},
    {"nombre": "Luis", "edad": 25}
]

personas_ordenadas = sorted(personas, key=lambda p: p["edad"])
print(personas_ordenadas)

