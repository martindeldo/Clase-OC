Precio=input("ingresa precio original de producto ")
prec=int(Precio)
Descuento=input("Ingresa porcentaje de descuento")
desc=int(Descuento)
Montodesc=prec*desc/100
print(Montodesc)
Total=prec-Montodesc
print(Total)