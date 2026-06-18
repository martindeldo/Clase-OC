
def mayor_de_tres(n1, n2, n3):
    if n1>n2 and n1>n3:
        return n1
    if n2>n3 and n2>n1:
        return n2
    
    if n3>n2 and n3>n1:
        return n3
num1=int(input("ingresa n1"))
num2=int(input("ingresa n2"))
num3=int(input("ingresa n3"))

print(mayor_de_tres(num1, num2, num3))



        

    
