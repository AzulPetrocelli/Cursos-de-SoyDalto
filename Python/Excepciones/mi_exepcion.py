#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste un error")
        
#Lanzando mi pripia excepcion con la palabra clave raise
#raise MiException("Jajajajaja, persona poco culta")

#Manejando mi excepcion
try:
    raise MiExcepcion("Jajajajaja, persona poco culta")
except:
    print("como vas a cometer ese error")
