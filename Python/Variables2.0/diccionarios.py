#Creando diccionarios con dict() (unica porma de crear diccionarios vacios)
diccionario = dict(nombre = "Azul", apellido="Petrocelli")

#Las tuplas y los conjuntos INMUTABLES(con frozenset) pueden ser claves
diccionario = {("nombre", "apellido") : "Azul Petrocelli"}
diccionario = {frozenset(["nombre", "apellido"]) : "Azul Petrocelli"}

#Las listas y conjuntos NO pueden ser claves
# diccionario = {["nombre", "apellido"] : "Azul Petrocelli"}
# diccionario = {{"nombre", "apellido"} : "Azul Petrocelli"}

#Creando diccionarios con fromkeys valor por defecto: None 
diccionario = dict.fromkeys(["nombre", "apellido"]) # {'nombre': None, 'apellido': None}
#OJO fromkeys es un metodo por eso usamos dict

#Creando diccionarios con fromkeys cambiando el valor por defecto a "No se"
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")

#Creando diccionarios con fromkeys cambiando el valor por defecto a 0 
diccionario = dict.fromkeys("ABCDE", 0) # {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
