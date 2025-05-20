condicion = True
condicion2 = True

if condicion:
    print("se ejecuta si la condicion es verdadera")
else:
    print("se ejecuta si la condicion NO es verdadera")
print("esto no forma parte del if ni del else")

#if anidado
if condicion:
    if condicion2:
        print("se ejecuta si el if anidado es verdadera")
    else:
        print("se ejecuta si el if anidado es falso")
else:
    print("se ejecuta si la condicion NO es verdadera")