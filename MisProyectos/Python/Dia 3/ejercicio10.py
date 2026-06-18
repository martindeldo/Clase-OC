def puede_votar(edad):
    if edad>=18:
        return "puede votar"
    else:
        return "no puede votar"
ed=int(input("ingresa edad")) 
print(puede_votar(ed))  
    