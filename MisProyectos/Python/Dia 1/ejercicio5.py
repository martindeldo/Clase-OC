from copy import error


while True:
    try:
        Notas1=int(input("ingresa nota"))
        break
    except Exception as e:
        print("el error es",error(e))

while True:

    try:
        Notas2=int(input("ingresa nota"))
        break
    except Exception as f:
        print("el error es", error(f))

while True:
    try:

        Notas3=int(input("ingresa nota"))
        break
    except Exception as g:
        print("el error es", error(g))
Promedio=(Notas1 + Notas2 + Notas3)/3
print(Promedio)