from copy import error


while True:
    try:
        Celsius=int(input("ingresa los grados celsius"))
        break
    except Exception as h:
        print("el error es",error(h))

Fahreinheit=(Celsius*9/5)+32
print(Fahreinheit)
