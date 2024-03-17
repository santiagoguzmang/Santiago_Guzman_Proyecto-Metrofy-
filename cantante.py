import uuid 
class Cantante:
    def __init__(self, identificador, nombre,email, nombre_usuario,tipo='musician'):
        self.identificador = identificador
        self.nombre = nombre
        self.email = email
        self.nombre_usuario = nombre_usuario
        self.tipo = tipo

    def __str__(self) -> str:
        return f"id: {self.identificador}\nNombre: {self.nombre}\nTipo: {self.tipo}\n"
    
    @classmethod
    def nuevo_musico(cls,usuarios):
        from funciones import carga_datos

        usuarios_real = carga_datos(usuarios)
        
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese su correo electronico: ")
        nombre_usuario = input("Ingresa tu nombre de usuario: ")
        tipo = "musician" 

        nuevo_usuario = {
        "identificador": str(uuid.uuid4),
        "nombre": nombre,
        "email": correo,
        "nombre_usuario": nombre_usuario,
        "tipo": tipo
        }

        usuarios_real.append(nuevo_usuario)
        return usuarios_real