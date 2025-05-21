#Pedirle un dato al usuario, devuelve un String SIEMPRE
nombre = input("Ingrese su nombre: ") 

edad = int(input("ingrese su edad: ")) #convertimos la entrada del input de string a int

altura = float(input("Ingrese su altura en metros (con .): "))

print(f"Hola {nombre} de {altura} metros de altura y {edad} años de edad")

#NOTA: si no cambiamos los valores del input pueden pasar cosas como estas
#2 * 5 = 10
#"2" * 5 = "22222"