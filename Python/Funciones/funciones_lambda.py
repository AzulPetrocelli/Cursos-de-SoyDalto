#Creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : 2*x
print(multiplicar_por_dos(2))


#Creando la misma funcion sin lambda
def multiplicar_por_dos(x):
    return x*2

print(multiplicar_por_dos(2))

numeros = [1,2,3,4,5,6,7,8,9,10]

#Creando una funcion que diga si un numero es par
def es_par(num):
    if(num%2==0):
        return True

#Usando filter con una funcion comun
numeros_pares = filter(es_par, numeros) #retorna un objeto con los numeros que cumplen la funcion
print(numeros_pares)
print(list(numeros_pares)) #convierto el objeto a lista y lo muestro

#Usando filter con una funcion lambda
numeros_pares = filter(lambda num : num%2 == 0, numeros)
print(numeros_pares)
print(list(numeros_pares))