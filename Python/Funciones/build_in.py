numeros = [4,2,57,8,9,7]

#Determinar el numero mas grande de un iterable(lista, tupla, conjunto)
num_mas_alto = max(numeros)

#Determinar el numero mas chico de un iterable(lista, tupla, conjunto)
num_mas_bajo = min(numeros)

#Redondeando a 6 decimales
numero_redondeado = round(12.12345678, 6)
print(numero_redondeado)

#retornar False si le pasamos --> 0, vacio, [], False, None
# para cualquiero otro dato da true
resulado = bool(0)
resulado = bool()
resulado = bool([])
resulado = bool(False)
resulado = bool(None)

#Retorna True, si TODOS los valores son verdaderos
resulado_all = all([123, "True", True]) #True
resulado_all = all([123, "True", False]) #False
resulado_all = all([123, "True", []]) #False
resulado_all = all([123, "True", 0]) #False
resulado_all = all([123, "True", None]) #False

#Sumatoria de numeros de un iterable
suma_total = sum(numeros)

