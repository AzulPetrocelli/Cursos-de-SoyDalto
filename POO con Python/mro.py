#MRO (Method Resolution Order)
class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    pass
        
class C(A):
    def hablar(self):
        print("Hola desde C")
        
class D(B,C):
    pass

#Si una clase sobreescribe un metodo heredado, el MRO le va a dar prioridad a la clase de donde la estemos llamando 
c = C()
c.hablar() #Hola desde C

#El MRO escala, busca el metodo segun el orden en que heredamos, primero en B al no encontrar nada busca en C
d = D()
d.hablar() #Hola desde C
#Nota: si no lo encontraba en C se iba a ir a buscar el metodo en A

# Niveles que sigue el MRO en este caso
#     A
#   /  \
#  B    C
#  \   /
#    D
# D>B>C>A>Objeto instanciado

#Saber que orden sigue el MRO para una clase en particular
print(D.mro())

class A:
    pass
        
class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    pass
        
class C(F):
    pass
        
class D(B,C):
    pass

d = D()
d.hablar() #Hola desde F

# Niveles que sigue el MRO en este otro caso
#    A   F
#   |   |
#  B    C
#  \   /
#    D
# D>B>A>C>F>Objeto instanciado