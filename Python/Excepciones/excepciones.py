def sumar_dos():
    while True:
        #pidiendo numeros
        a = input("Ingresa el primer numero: ")
        b = input("Ingresa el segundo numero: ")
        
        #Intentando convertirlos a enteros y sumarlos
        try: 
            resultado = int(a) + int(b)
        #Si lanzo una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("Hubo un error trata de ingresar valores correspondientes")
            #Mostrar el nombre del error y su descripcion
            print(f"{type(e).__name__}: {e}")
        #Si todo salio bien terminamos el bucle
        else:
            break
        #Sin importar el resultado ejecuta esto
        finally:
            print("Esto se ejecuta siempre")
        
    return resultado

#Mostrando el resultado
print(sumar_dos())