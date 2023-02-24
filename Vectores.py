#Un vector es una estructura de código que agrupo distintos datos en una variable
#Una de las funciónes principales de los vectores en que son iterables
#Tenemos cuatro estructuras Lista, Tupla, Conjunto y Diccionario (list, tuple, set, dict)

#Creando una lista

lista = ['Programación', True, 30]

#Cuando se crea una lista esta esta ordenada en indices y cada elemento se cuenta desde el 0
#También se puede llamar desde un indice negativo, empezondo por el último dato

print(lista[0])
print(lista[-1])
print(lista[0:2])

#Creando una tupla, las tuplas son vectores inmutables. 
#Se puede iterar una tupla desde su indice

tupla = (1, 1, 2, 3, 5, 8)

'tupla[0]+= 2' #No se modifican

print(tupla)
print(tupla[3])
print(tupla[0:3])

#Creando un conjunto, los conjuntos son inmutables, no estan indexados y no aceptan duplciados
#No se puede iterar por su indice

conjunto = {'String', 'Python', 5.0, False}

print(conjunto)

#Creando un diccionario, los diccionarios son mutables, no aceptan duplicados. 
#No se accede al indice, en este caso se utilizan claves únicas para poder imprimir los valores

diccionario = {
    "cmc": 'CamelCase',
    "snke": 'sanake_case',
    "lng":  'Python'
}

print(diccionario['cmc'])
