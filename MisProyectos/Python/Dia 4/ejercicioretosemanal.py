saldo=1000
def verificar_pin(pin_ingresado):
    if pin_ingresado=="1234":
        return True
    else:
        return False

def retirar(cantidad):
    if cantidad>saldo:
        saldo=saldo-cantidad
        print("retiro exitoso")
    else:
        print("fondos insuficientes") 
print("bienvenido")         
pin=input("ingresa tu pin")     
if verificar_pin(pin):  
    print("corrrecto saldo actual", saldo)
    try:
        monto_str=input=input("cuanto desea retirar")
        monto=int(monto_str)
        print(retirar(monto))
    except ValueError:
        print("error ingesaun numero valido")
else:
    print("pin en camino")        




    
    



    

