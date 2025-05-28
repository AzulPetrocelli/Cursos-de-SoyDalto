import re
#detectando un numero Caba y ocultandolo
texto = "Hola Azul, mi numero es: +54 11 4321-4321"

pattern = r"\+\d{1,3}\s\d{2}\s\d{4}-\d{4}"

remplazo = re.sub(pattern, "(Numero oculto)", texto)
print(remplazo)