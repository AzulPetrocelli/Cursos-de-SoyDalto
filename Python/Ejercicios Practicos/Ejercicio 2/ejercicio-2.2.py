#Creando una funcion que nos devuelve los numeros
# primos entre 0 y el argumento que le pasemos

#Funcion que retorna True si un numero es primo
def es_primo(num):
    for i in range(2,num-1):                       # Iteramos en un rango de 2 a num-1 (cualquier numero es divisible por dos y por si mismo)
        if num%i == 0: return False                # Si es divisible por algun numero no es primo 
    return True

resultado = es_primo(8)
print(resultado)

#Funcion que retorna una lista de numeros primos hasta un numero dado
def primos_hasta(num):
    lista_de_primos = []
    
    for i in range(1, num+1):                      # Iteramos en un rango de 1 a num+1 (para que cuente el ultimo primo)
        if(es_primo(i)): lista_de_primos.append(i) # Verificamos que el valor sea primo

    return lista_de_primos                         # Retornamos la lista de primos

resultado = primos_hasta(7)
print(resultado)