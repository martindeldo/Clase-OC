from copy import error


while True:
    try:
        Base=int(input("ingresa base del triangulo"))
        break
    except Exception as f:
        print ("El error es", error (f))

while True:
    try:
        Altura=int(input("ingresa altura del triangulo"))
        break
    except Exception as e:
        print ("el error es",error(e))
Area=Base*Altura
print(Area)
