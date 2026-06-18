from copy import error


while True:
    try:

        cuenta=int(input ("Ingresa total de la cuenta"))
        break

    except Exception as e:
        print("cometiste un error", error(e))

while True:
    try:
        Propina=int(input ("Ingresan porcentaje de propina"))    
        break

    except Exception as f:
        print("Cometiste un error", error(f)) 

total_propina=cuenta*Propina/100
print(total_propina)
Cuenta_total=cuenta+total_propina
print(Cuenta_total)






