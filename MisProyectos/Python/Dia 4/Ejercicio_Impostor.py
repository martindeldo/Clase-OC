from copy import error
import random
import time
cant= int(input("ingresa la cantidad de jugadores mayor a 2"))
 
lista_jugadores=[]
lista_palabras=["Ganso","Oso","Leon","Iguana","Caballo","Tigre","Sapo","Ciervo","Elefante","Tiburon"]
for i in range (cant):
    Nomb = input("ingresa el nombre")
    lista_jugadores.append(Nomb)
impostor=random.choice(lista_jugadores)
palabra=random.choice(lista_palabras)
print ("reparto de jugadores")
for f in range (lista_jugadores):
    if Nomb==impostor:
        print("impostor")
    else:
        print(palabra)



