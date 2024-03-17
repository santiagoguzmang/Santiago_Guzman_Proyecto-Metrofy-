
import requests
import json
from cantante import Cantante
from escucha import Escucha
from album import Album
from playlist import Playlist
import uuid

#RUTAS ARCHIVOS
RUTA_USUARIOS = "usuarios.json"
RUTA_ALBUM = "albums.json"
RUTA_PLAYLIST = "playlist.json"

#FUNCIONES ARCHIVOS
def actualizar_datos(archivo_actualizado,ruta_archivo):
    with open(ruta_archivo,"w") as file:
        json.dump(archivo_actualizado,file,indent=4)

def carga_datos(route_archive):
    # Carga de datos desde el archivo JSON
    try:
        with open(route_archive, 'r') as file:
            usuarios_data = json.load(file)
    except FileNotFoundError:
        print(f"El archivo {route_archive} no existe. Se devolverá una lista vacía.")
        usuarios_data = []
    except json.JSONDecodeError:
        print("Error al decodificar datos JSON. Se devolverá una lista vacía.")
        usuarios_data = []

    return usuarios_data

def guardar_data(objetos,archivo: str):
    objetos_serializados = []
    for obj in objetos:
        if hasattr(obj,'__dict__'):
            objetos_serializados.append(obj.__dict__)
        else:
            print("Ha ocurrido un error")
    
    with open(archivo,'w') as file:
        json.dump(objetos_serializados,file,indent=4)

def original_datos():
    #URL DE DATOS
    url_usuarios = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json"
    url_albums = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json"
    url_playlist = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json"
    #RECORRIENDO DATOS
    response_usuarios = requests.get(url_usuarios)
    data_usuarios = response_usuarios.json()

    response_albums = requests.get(url_albums)
    data_albums = response_albums.json()

    response_playlist = requests.get(url_playlist)
    data_playlists = response_playlist.json()

    #LISTA GUARDAR DATOS
    albums = []
   
#Guardando los albunes
    for data_album in data_albums:
        album = Album(data_album['id'],data_album['name'],data_album['description'],data_album['cover'],data_album['published'],data_album['genre'],data_album['artist'],data_album['tracklist'])
        albums.append(album)
    playlists = []
    
    for data_playlist in data_playlists:
        playlist = Playlist(data_playlist['id'],data_playlist['name'],data_playlist['description'],data_playlist['creator'],data_playlist['tracks'])
        playlists.append(playlist) 
    usuarios = []
    for data in data_usuarios:
        if data['type'] == 'musician':
            musico = Cantante(data['id'],data['name'],data['email'],data['username'])
            usuarios.append(musico)
        else:
            escucha = Escucha(data['id'],data['name'],data['email'],data['username'])
            usuarios.append(escucha)
    
    guardar_data(albums,RUTA_ALBUM)
    guardar_data(playlists,RUTA_PLAYLIST)
    guardar_data(usuarios,RUTA_USUARIOS)

def registrar(nombre, usuario, correo, tipoUsuario, RUTA_USUARIOS):

    usuarios_archivo = carga_datos(RUTA_USUARIOS)
    if tipoUsuario.lower() == "escucha":
        
        nuevo_usuario = {
                'id': str(uuid.uuid4()),
                'usuario': usuario,
                'firstName': nombre,
                'email': correo,
                'type': 'listener',
            }
        
        nuevo_usuarios_archivo = usuarios_archivo.append(nuevo_usuario)
        return nuevo_usuarios_archivo



    if tipoUsuario.lower() == "cantante":
        
        nuevo_usuario = {
                'id': str(uuid.uuid4()),
                'usuario': usuario,
                'firstName': nombre,
                'email': correo,
                'type': 'musician',
            }
        nuevo_usuarios_archivo = usuarios_archivo.append(nuevo_usuario)
        return nuevo_usuarios_archivo
    
    else: 
         print("ERROR. El tipo de usuario tiene que ser cantante o escucha")
    


def buscar_perfil(nombre_a_buscar):

    usuarios_data = carga_datos(RUTA_USUARIOS)

    encontrado = False
    for data in usuarios_data:
        if nombre_a_buscar.lower() == data['nombre'].lower():
            encontrado = True
            print(data)
    
    if encontrado == False:
        print("Ese nombre no se encuetra anexado a ningun usuario")


def cambiar_perfil(nombre_usuario_a_cambiar):
    try:
        usuarios_data = carga_datos(RUTA_USUARIOS)
        usuario_encontrado = False
        for data in usuarios_data:
            if nombre_usuario_a_cambiar.lower() == data['nombre'].lower():
                usuario_encontrado = True
                print(f"Se ha encontrado el usuario con el nombre {nombre_usuario_a_cambiar}")
                print("A continuación vamos a pedir la nueva información a actualizar")
                print("")
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_correo = input("Nuevo correo: ")
                data['nombre'] = nuevo_nombre
                data['email'] = nuevo_correo
                actualizar_datos(usuarios_data, RUTA_USUARIOS)
                print("Perfil actualizado correctamente.")
                break

        if not usuario_encontrado:
            print("ERROR: El nombre de usuario no se ha encontrado en la base de datos.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

def borrar_perfil(nombre_del_usuario_a_borrar):

    usuario_data = carga_datos(RUTA_USUARIOS)
    encontrado = False

    for data in usuario_data:
        if data['nombre'] == nombre_del_usuario_a_borrar:
            encontrado = True
            usuario_data.remove(data)
            print("Usuario eliminado correctamente")
            actualizar_datos(usuario_data, RUTA_USUARIOS)
    if encontrado == False:
        print("No se ha encontrado el nombre")

def buscador1(RUTA_ALBUMS, RUTA_USUARIOS):

    # Carga de datos
    data_albums = carga_datos(RUTA_ALBUMS)
    data_usuarios = carga_datos(RUTA_USUARIOS)

    # Búsqueda del nombre del álbum
    nombre_album = input("Ingrese el nombre del álbum: ")

    # Búsqueda del nombre de usuario
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario_identificador = None
    nombre_usuario_encontrado = False

    for user in data_usuarios:
        if user['nombre_usuario'] == nombre_usuario:
            nombre_usuario_encontrado = True
            usuario_identificador = user['identificador']
            break

    if not nombre_usuario_encontrado:
        print("No se ha encontrado el nombre de usuario en la base de datos")
        return

    # Búsqueda del álbum
    nombre_album_encontrado = False
    cancion_a_escuchar = False

    for album in data_albums:
        if nombre_album == album['nombre']:
            nombre_album_encontrado = True
            print("Se encontro el album")
            print("")
            print("Estas son las canciones del album: ")
            print("")
            for track in album['tracklist']:
                print(track['name'], track['duration'])

            cancion = input("Ingrese el nombre de la cancion que desea escuchar: ").lower()

            for track in album['tracklist']:
                if cancion == track['name'].lower():
                    cancion_a_escuchar = True
                    print(f"sonando: {track['name']}")

                    if 'reproducciones' in track:
                        track['reproducciones'].append(usuario_identificador)
                    else:
                        track['reproducciones'] = [usuario_identificador]

                    break

    if not nombre_album_encontrado:
        print("Ha ocurrido un error en la búsqueda. Chequea la información dada")
        return

    # Búsqueda de la canción
    if not cancion_a_escuchar:
        print("No se ha encontrado la canción a escuchar del artista")
        return

    # Actualización de datos
    actualizar_datos(data_albums, RUTA_ALBUMS)


def buscador2(RUTA_ALBUMS, RUTA_USUARIOS):

    # Carga de datos
    data_albums = carga_datos(RUTA_ALBUMS)
    data_usuarios = carga_datos(RUTA_USUARIOS)

    # Búsqueda del nombre del cantante
    nombre_artista = input("Indique el nombre del cantante: ")

    # Búsqueda del nombre de usuario
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario_identificador = None
    nombre_usuario_encontrado = False

    for user in data_usuarios:
        if user['nombre_usuario'] == nombre_usuario:
            nombre_usuario_encontrado = True
            usuario_identificador = user['identificador']
            break

    if not nombre_usuario_encontrado:
        print("No se ha encontrado el nombre de usuario en la base de datos")
        return

    # Búsqueda del cantante
    cantante_encontrado = False

    for usuario in data_usuarios:
        if usuario['nombre'] == nombre_artista and usuario['tipo'] == "musician":
            cantante_encontrado = True
            break

    if not cantante_encontrado:
        print(f"No se ha encontrado al cantante {nombre_artista}")
        return

    # Búsqueda del álbum
    album_a_escuchar = False

    album_artista = [album for album in data_albums if album['artista'] == usuario['identificador']]
    print("Estos son los albums que tiene:")
    print("")
    for album in album_artista:
        print(album['nombre'])

    album_escuchar = input("Indique el album que desea escuchar: ")

    for album in album_artista:
        if album_escuchar == album['nombre']:
            album_a_escuchar = True
            for track in album['tracklist']:
                print(track['name'], track['duration'])

            cancion = input("Ingrese el nombre de la cancion que desea escuchar: ").lower()

            for track in album['tracklist']:
                if cancion == track['name'].lower():
                    cancion_a_escuchar = True
                    print(f"sonando: {track['name']}")

                    if 'reproducciones' in track:
                        track['reproducciones'].append(usuario_identificador)
                    else:
                        track['reproducciones'] = [usuario_identificador]

    if not album_a_escuchar:
        print("No se encontro el album en la lista de albums del artista")
        return

    # Búsqueda de la canción
    if not cancion_a_escuchar:
        print("No se encontro la cancion en la lista de canciones del artista")
        return

                        
def buscador3(RUTA_ALBUMS, RUTA_PLAYLIST, RUTA_USUARIOS):

    """
    Función que busca una playlist, una canción y la reproduce.

    Args:
        RUTA_ALBUMS (str): Ruta al archivo con datos de los álbumes.
        RUTA_PLAYLIST (str): Ruta al archivo con datos de las playlists.
        RUTA_USUARIOS (str): Ruta al archivo con datos de los usuarios.

    Returns:
        None.
    """

    # Carga de datos
    data_albums = carga_datos(RUTA_ALBUMS)
    data_usuarios = carga_datos(RUTA_USUARIOS)
    data_playlist = carga_datos(RUTA_PLAYLIST)

    # Búsqueda del nombre de usuario
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    usuario_identificador = None
    nombre_usuario_encontrado = False

    for user in data_usuarios:
        if user['nombre_usuario'] == nombre_usuario:
            nombre_usuario_encontrado = True
            usuario_identificador = user['identificador']
            break

    if not nombre_usuario_encontrado:
        print("No se encontró el nombre de usuario en la base de datos")
        return

    # Búsqueda de la playlist
    playlist_encontrada = False
    cancion_a_escuchar = False

    nombre_playlist = input("Indique el nombre de la Playlist: ")
    print("")
    print("Estas son las canciones de la playlist: ")
    print("")

    for playlist in data_playlist:
        if nombre_playlist == playlist['nombre']:
            playlist_encontrada = True
            track_playlist = playlist['tracks']

            for track_id in track_playlist:
                for album in data_albums:
                    for track in album['tracklist']:
                        if track_id == track['id']:
                            print(track['name'])

            cancion = input("Indique la canción a escuchar: ").lower()

            for track in album['tracklist']:
                if cancion == track['name'].lower():
                    cancion_a_escuchar = True
                    print(f"sonando: {track['name']}")

                    if 'reproducciones' in track:
                        track['reproducciones'].append(usuario_identificador)
                    else:
                        track['reproducciones'] = [usuario_identificador]

                    break

    # Actualización de datos
    actualizar_datos(data_albums, RUTA_ALBUMS)

    if not playlist_encontrada:
        print("No se encontró la Playlist a buscar")
        return

    if not cancion_a_escuchar:
        print("No se ha encontrado la canción del artista a escuchar")

def likes_musico(data_usuarios):


    nombre_usuario = input("Indica tu nombre de usuario: ")
    nombre_artista = input("Indique el nombre de usuario del artista: ")

    userA = next((user for user in data_usuarios if user['nombre_usuario'] == nombre_usuario), None)
    userB = next((user for user in data_usuarios if user['nombre_usuario'].lower() == nombre_artista.lower() and user['tipo'] == "musician"), None)

    if userA is None or userB is None:
        print("No se encontró el nombre de usuario o el artista en la base de datos.")
        return

    if 'likes' not in userB:
        userB['likes'] = []

    if userA['identificador'] in userB['likes']:
        print("No puedes dar likes dos veces.")
        remover = input("¿Quieres quitar el like? (si/no): ")
        if remover.lower() == "si":
            userB['likes'].remove(userA['identificador'])
            print("Like eliminado con éxito.")
        else:
            print("Operación cancelada.")
    else:
        userB['likes'].append(userA['identificador'])
    
    actualizar_datos(data_usuarios, RUTA_USUARIOS)

def likes_album(data_usuarios, data_albums):


    nombre_usuario = input("Indique su nombre de usuario: ")
    id_usuario = None

    for user in data_usuarios:
        if user['nombre_usuario'] == nombre_usuario:
            id_usuario = user['identificador']
            break
    else: 
        print("No se encontró el nombre de usuario en la base de datos.")
        return

    nombre_album = input("Indique el nombre del álbum: ")
    for album in data_albums:
        if album['nombre'] == nombre_album:
            if 'likes' not in album:
                album['likes'] = [id_usuario]
            elif id_usuario in album['likes']:
                print("No puedes dar like dos veces.")
            else:
                album['likes'].append(id_usuario)
            
            actualizar_datos(data_albums, RUTA_ALBUM)
            print("Like agregado con éxito.")
            return

    print("No se encontró el álbum en la base de datos.")

def likes_cancion(data_usuarios, data_albums):


    nombre_usuario = input("Indique su nombre de usuario: ")
    id_usuario = None

    # Buscar el ID del usuario
    for usuario in data_usuarios:
        if usuario['nombre_usuario'] == nombre_usuario:
            id_usuario = usuario['identificador']
            break
    else: 
        print("No se encontró el nombre de usuario en la base de datos.")
        return

    nombre_album = input("Indique el nombre del álbum: ")
    for album in data_albums:
        if album['nombre'] == nombre_album:
            # Mostrar las canciones del álbum
            print("Canciones del álbum:")
            for track in album['tracklist']: 
                print(track['name'])
                print(track['duration'])
                print("")

            # Solicitar el nombre de la canción
            nombre_cancion = input("Ingrese el nombre de la canción: ")
            for track in album['tracklist']:
                if track['name'] == nombre_cancion:
                    if 'likes' not in track:
                        track['likes'] = [id_usuario]
                    elif id_usuario in track['likes']:
                        print("No puedes dar like dos veces.")
                        remover = input("¿Quieres quitar el like? (si/no): ")
                        if remover.lower() == "si":
                            track['likes'].remove(id_usuario)
                            print("Like eliminado con éxito.")
                        else:
                            pass
                    else:
                        track['likes'].append(id_usuario)
            
            actualizar_datos(data_albums, RUTA_ALBUM)
            print("Likes actualizados correctamente.")
            return

    print("No se encontró el álbum en la base de datos.")

def likes_playlist(data_usuarios, data_playlist):

    nombre_usuario = input("Indique su nombre de usuario: ")
    id_usuario = None

    # Buscar el ID del usuario
    for usuario in data_usuarios:
        if usuario['nombre_usuario'] == nombre_usuario:
            id_usuario = usuario['identificador']
            break
    else: 
        print("No se encontró el nombre de usuario en la base de datos.")
        return

    nombre_playlist = input("Indique el nombre de la playlist: ")
    for playlist in data_playlist:
        if playlist['nombre'] == nombre_playlist:
            if 'likes' not in playlist:
                playlist['likes'] = [id_usuario]
            elif id_usuario in playlist['likes']:
                print("No puedes dar like dos veces.")
                remover = input("¿Quieres quitar el like? (si/no): ")
                if remover.lower() == "si":
                    playlist['likes'].remove(id_usuario)
                    print("Like eliminado con éxito.")
                else:
                    pass
            else:
                playlist['likes'].append(id_usuario)
            
            actualizar_datos(data_playlist, RUTA_PLAYLIST)
            print("Likes actualizados correctamente.")
            return

    print("No se encontró la playlist en la base de datos.")

def mayores_streams_musicos(lista_usuarios, lista_albums):
    array_de_cantidad_de_streams_de_todos_los_musicos = []

    for user in lista_usuarios:
        if user['tipo'] == "musician":
            id_musico = user['identificador']
            cant_streams = 0

            for album in lista_albums:
                if album['artista'] == id_musico:
                    for track in album['tracklist']:
                        if 'reproducciones' in track:
                            cant_streams += track['reproducciones']

            array_de_cantidad_de_streams_de_todos_los_musicos.append((user['nombre'], cant_streams))
    print(array_de_cantidad_de_streams_de_todos_los_musicos)
    array_de_cantidad_de_streams_de_todos_los_musicos.sort(key=lambda x: x[1], reverse=True)
    
    top_musicos = []
    for i in range(min(5, len(array_de_cantidad_de_streams_de_todos_los_musicos))):
        top_musicos.append(array_de_cantidad_de_streams_de_todos_los_musicos[i])

    return top_musicos

def mayores_streams_albums(lista_albums):
    array_de_cantidad_de_streams_de_todos_los_albums = []

    for album in lista_albums:
        cant_reproducciones_en_cada_album = 0
        for track in album['tracklist']:
            if 'reproducciones' in track:
                cant_reproducciones_en_cada_album += track['reproducciones']

        array_de_cantidad_de_streams_de_todos_los_albums.append((album['nombre'], cant_reproducciones_en_cada_album))
    
    array_de_cantidad_de_streams_de_todos_los_albums.sort(key=lambda x: x[1], reverse=True)

    for i in range(min(5, len(array_de_cantidad_de_streams_de_todos_los_albums))):
        print(f"{array_de_cantidad_de_streams_de_todos_los_albums[i][0]}: {array_de_cantidad_de_streams_de_todos_los_albums[i][1]} streams")

def mayores_streams_canciones(lista_albums):


    # Inicialización de variables
    array_streams_canciones = []

    # Recorrido de los álbumes
    for album in lista_albums:
        # Recorrido de las canciones del álbum
        for track in album['tracklist']:
            # Contador de streams por canción
            streams_cancion = 0
            # Si la canción tiene información de streams
            if 'reproducciones' in track:
                # Se suman los streams de la canción
                streams_cancion += track['reproducciones']

            # Se agrega el nombre de la canción y la cantidad de streams a la lista
            array_streams_canciones.append((track['name'], streams_cancion))

    # Ordenamiento por cantidad de streams (mayor a menor)
    array_streams_canciones.sort(key=lambda x: x[1], reverse=True)

    # Impresión de las 5 canciones con más streams
    for i in range(min(5, len(array_streams_canciones))):
        print(f"{array_streams_canciones[i][0]}: {array_streams_canciones[i][1]} streams")

def mayores_streams_escuchas(lista_usuarios, lista_albums):
    array_de_cantidad_de_streams_de_todos_los_usuarios = []
     
    for user in lista_usuarios:
        cant_streams_usuario = 0
        if user['tipo'] == 'listener':
            id_usuario = user['identificador']

            for album in lista_albums:
                for track in album['tracklist']:
                    if 'reproducciones' in track and track['reproducciones'] == id_usuario:
                        cant_streams_usuario += 1

            array_de_cantidad_de_streams_de_todos_los_usuarios.append((user['nombre'], cant_streams_usuario))

    array_de_cantidad_de_streams_de_todos_los_usuarios.sort(key=lambda x: x[1], reverse=True)

    for i in range(min(5, len(array_de_cantidad_de_streams_de_todos_los_usuarios))):
        print(f"{array_de_cantidad_de_streams_de_todos_los_usuarios[i][0]}: {array_de_cantidad_de_streams_de_todos_los_usuarios[i][1]} streams")
              

        

        
            

        



    

        

    
        

                            









    
                        







            












    




    

    