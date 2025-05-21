#A) Pedirle al usuario que diga cualquier texto real y:
cantidad_de_palabras_por_segundo = 2
frase = input("Decime una frase y calculo cuanto tardarias en leerla: ")

#cuantas palabras dijo
cantidad_de_palabras = len(frase.split(" "))
print(f"En la frase hay {cantidad_de_palabras} palabras")

#Cuanto tardaria en decir la frase?
duracion_en_segundos = cantidad_de_palabras * 100 // cantidad_de_palabras_por_segundo / 100
print(f"Tardarias {duracion_en_segundos} segundos en decir esa frase")

#B) Si tardan mas de un minuto mostrar un mensaje
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")

#C) Cuanto tardaria dalto que habla un 30% mas rapido
cantidad_de_palabras_por_segundo_dalto = 1.3

duracion_en_segundos_dalto = duracion_en_segundos * 100 // cantidad_de_palabras_por_segundo_dalto/100
print(f"Dalto tardaria {duracion_en_segundos_dalto} segundos en decir esa frase")
