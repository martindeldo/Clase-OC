
from copy import error

while True:
    try:
        Numero=int(input("ingresa un numero entero"))

        break

    except Exception as e:

        print("el error es ", error(e))
        
if Numero%2== 0:
    print("par")

else:
    print("impar")