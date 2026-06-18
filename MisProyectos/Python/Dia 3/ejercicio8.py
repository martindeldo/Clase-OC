def calcular_precio_final(precio,descuento):
    descuentofinal=precio*descuento/100
    precio=precio-descuentofinal
    return precio
pr=int(input("precio:"))
des=int(input("descuento:"))
print (calcular_precio_final(pr, des))