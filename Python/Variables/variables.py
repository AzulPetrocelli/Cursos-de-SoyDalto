#Definiendo una variable con canelCase
nombreCompleto = "Azul Martin Petrocelli"

#Definiendo una variable con snakeCase (Recomendada por Python)
nombre_Completo = "Azul Martin Petrocelli"

#Concatenar con +
bienvenida1 = "Hola " + nombreCompleto + " ¿Como estas?"

#Concatenar con f-strings
bienvenida2 = f"Hola {nombre_Completo} ¿Como estas?"

#Operadores de pertenencia (in / not in)
print("Hola" in bienvenida2)
print("Hola" not in bienvenida2)
