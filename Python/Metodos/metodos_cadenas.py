cadena1 = "Hola soy azul"
cadena2 = "Bienvenido a mis apuntes de codigo"

#FUNCIONES------------------------------------------------
#Imprimir por pantalla
print(cadena1)

#Devuelve lista de atributos validos para un objeto (en este caso una cadena)
lista_de_atributos = dir(cadena1)

#Devuelve la cantidad de caracteres de una cadena
contar_caracteres = len(cadena1)

#METODOS--------------------------------------------------

#Convierte a mayusculas
mayus = cadena1.upper()

#Convierte a minusculas
minus = cadena1.lower()

#Primera letra en mayuscula lo demas en minuscula
primer_letra_mayus = cadena1.capitalize()

#Buscamos una cadena dentro de otra, retorna la primer coincidencia si no hay devuelve -1
busqueda_find = cadena1.find("Hola") #0
busqueda_find = cadena1.find("hola") #-1 --> recorda que Python es case sensitive

#Buscamos una cadena dentro de otra, si no la encuentra nos devuelve una excepcion
busqueda_index = cadena1.index("Hola") #0
#busqueda_index = cadena1.index("hola") #Exepcion

#si en numerico
es_numerico = cadena1.isnumeric() #False
es_numerico = "12344".isnumeric() #True

#Si es alfanumerico (de a-z y A-Z sin espacios)
es_alfanumerico = cadena1.isalpha() #False
es_alfanumerico = "ABC".isalpha() #True

#Buscamos una cadena dentro de otra, devuelve cuantas veces coincide
contar_coincidencias = cadena1.count("Hola")
contar_coincidencias = cadena1.count("a")
contar_coincidencias = cadena1.count("J")

#Verificamos si una cadena empieza con otra cadena dada
empieza_con = cadena1.startswith("Hola") #True
empieza_con = cadena1.startswith("hola") #False 

#Verificamos si una cadena termina con otra cadena dada
termina_con = cadena1.endswith("Azul") #False 
termina_con = cadena1.endswith("azul") #True

#Reemplaza una porcion de cadena dada con otra, si no hay coincidencias, nos devuelve la cadena sin cambios
cadena_nueva = cadena2.replace(" " , ", ") #remplaza los espacios por comas
print(cadena_nueva)

#Separar cadenas con la cadena que le pasemos, retorna una lista con esos valores separados
cadena_separada = cadena2.split(" ") #['Bienvenido', 'a', 'mis', 'apuntes', 'de', 'codigo']  separo por espacios
print(cadena_separada)
print(cadena_separada[0])
print(cadena_separada[1])
print(cadena_separada[2])
print(cadena_separada[3])
print(cadena_separada[4])
print(cadena_separada[5])
