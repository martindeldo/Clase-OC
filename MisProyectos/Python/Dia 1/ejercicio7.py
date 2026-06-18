from copy import error


while True:
    try:
        Horas=int(input("Ingresa las horas"))
        break
    except Exception as w:
        print ("El error es",error(w))

while True:
    try:
        Tarifa=int(input("ingresa tarifa"))
        break
    except Exception as e:
        print("el error es",error(e))

Salario=Horas*Tarifa
print(Salario)
