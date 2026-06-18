from copy import error


dolar=1000
while True:
    try:
     Cantidad=int(input("ingresa cantidad de dolares"))
     break
    except Exception as e:
       print("el error es", error(e))
       
Cambio=Cantidad*dolar
print (Cambio)
