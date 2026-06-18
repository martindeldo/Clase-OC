def crear_email (nombre, apellido):
    return (nombre, apellido, "empresa@gmail.com")
Nom= input ("Ingresa nombre")
Ape= input ("Ingresa apellido")
print(crear_email(Nom, Ape))