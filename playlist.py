import uuid

class Playlist:
    def __init__(self,identificacion,nombre,descripcion,creador,tracks):
        self.identificacion = identificacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.creador = creador
        self.tracks = tracks
        pass

    @classmethod
    def crear_playlist(cls, playlist_archivo):
        from funciones import carga_datos

        data_playlist = carga_datos(playlist_archivo)

        nombre = input("Indique el nombre: ")
        descripcion = input("Indique la descripcion: ")
        id_creador = input("Indique el id del usuario: ")


        nueva_playlist = {
            "identificacion": id_creador,
            "nombre": nombre,
            "descripcion": descripcion,
            "creador": id_creador,
            "tracks": []
        }

        data_playlist.append(nueva_playlist)
        print("")
        print("Ha creado la playlist exitosamente!")
        print("")
        return data_playlist
    



    
