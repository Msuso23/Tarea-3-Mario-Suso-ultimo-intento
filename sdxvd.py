class contacto():
    def __init__(self,nombre,tlf,correo):
        self.nombre=nombre
        self.tlf=tlf
        self.correo=correo

    def __str__(self):
        return f"{self.nombre} {self.tlf} {self.correo}"

class agenda():
    def __init__(self,contactos=[]):
        self.contactos=contactos
    

    def agregar(self,nuevocontacto):
        self.contactos.append(nuevocontacto)
    def lista(self):
        for listacontactos in self.contactos:
            print(listacontactos)
    def buscar(self):
        resultado= None
        nombre_user=input("Ingrese el nombre: \n")
        for nombres in self.contactos:
            if nombres==nombre_user:
                resultado=contacto
        print(resultado)