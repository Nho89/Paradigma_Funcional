#Paradigma funcional

# Función que multiplicará los números por 2:
def multiply_by_2(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
result = list(map(multiply_by_2, numbers))
print(result)  



# Función que verifica si un número es par:
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)
result_list = list(result)
print(result_list) 


#Aquí map() aplica una función a cada elemento, mostrando el enfoque declarativo del paradigma funcional.
def elevar_cuadrado(lista):
    return list(map(lambda x: x ** 2, lista))

numeros = [1, 2, 3, 4, 5]
print(elevar_cuadrado(numeros))


#Aquí lambda hace que la función sea más compacta, demostrando cómo la programación funcional ayuda a escribir código más corto y directo.
area = lambda base, altura: base * altura
print(area(5, 3))
