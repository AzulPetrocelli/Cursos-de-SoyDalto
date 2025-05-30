#OCR: Open/Close principle

#Las entidades de software, en nuesto caso, las
# clases los modulos, las funciones, etc. Tienen
# que estar abiertas para la extencion pero cerradas 
# para la modificacion. Es decir deberiamos poder 
# agregarles nuevas funcionalidades sin tener que 
# cambiar el codigo fuente de esta entidad

class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    #Si agrego un nuevo medio de comunicacion, creo una clase
    # que se ocupe notificar al cliente por ese medio particular
    def notificar(self):
        pass

#Si me dicen que debo notificar por SMS   
class NotificarPorSMS(Notificador):
    def notificar(self):
        print("Enviando mensaje SMS a {self.usuario.sms}")
        
#Ahora tambien debe poder notificar por MAIL    
class NotificarPorSMS(Notificador):
    def notificar(self):
        print("Enviando mail a {self.usuario.mail}")
        
#Ahora tambien debe poder notificar por WhatsApp    
class NotificarPorSMS(Notificador):
    def notificar(self):
        print("Enviando WhatsApp a {self.usuario.wsp}")
        
#Y asi agregamos funcionalidad sin modificar la primer clase 