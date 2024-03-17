import uuid

class Album:
    def __init__(self, identificacion, nombre, descripcion, link_portada, fecha, genero, artista, tracklist):
        self.identificacion = identificacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.link_portada = link_portada
        self.fecha = fecha
        self.genero = genero
        self.artista = artista
        self.tracklist = tracklist

    @classmethod
    def crear_album(cls, album_archivo):

        from funciones import carga_datos

        data_album = carga_datos(album_archivo)

        nombre = input("Indique el nombre: ")
        descripcion = input("Indique la descripcion: ")
        link_portada = input("Indique el link de la portada: ")
        fecha = input("Indique la fecha de publicacion: ")
        genero = input("Indique el genero del album: ")
        artista = input("Indique el nombre de usuario: ")

        intentos = int(input("Indique cuentas canciones va a colocar: "))
        for i in range(intentos):
            tracklist = []

            identificacion = str(uuid.uuid4())
            nombre = input("Indique el nombre de la cancion: ")
            duracion = input("Indique la duracion: ")
            link = input("Indique el link de la cancion: ")

            tracklist.append({
                "id": identificacion,
                "nombre": nombre,
                "duracion": duracion,
                "link": link
            })

        nuevo_album = {
            "id": str(uuid.uuid4),
            "nombre": nombre,
            "descripcion": descripcion,
            "link portada": link_portada,
            "fecha": fecha,
            "genero": genero,
            "artista": artista,
            "tracklist": tracklist,
            "likes":[]
        }

        data_album.append(nuevo_album)
        print("")
        print("Ha creado el album exitosamente!")
        print("")
        return data_album
