# Creando una funcion que muestre la serie fibonacci entre 0 y el numero dado

def fibbonacci(num):
    fibbonacci_lista = []
    ante_anterior,anterior= 0,1
    
    for i in range(num):
        if anterior > num : return fibbonacci_lista
        else: 
            fibbonacci_lista.append(anterior)
            ante_anterior,anterior = anterior, ante_anterior+anterior

resultado = fibbonacci(21)
print(resultado)