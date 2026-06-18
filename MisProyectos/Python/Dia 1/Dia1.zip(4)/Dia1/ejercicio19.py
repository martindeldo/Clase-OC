eleccion_programa = "Piedra"
eleccion_usuario = input("elige piedra, papel o tijera")

if eleccion_usuario=="Papel":
    print("¡Ganaste! papel envuelve a la piedra")
elif eleccion_usuario=="Piedra":
    print("Empate")
elif eleccion_usuario=="Tijera":
    print("Perdiste. Piedra rompe Tijera")