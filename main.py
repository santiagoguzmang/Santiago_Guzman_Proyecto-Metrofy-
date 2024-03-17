# RUTAS ARCHIVOS
from album import Album
from playlist import Playlist
from cantante import Cantante
from escucha import Escucha
from funciones import mayores_streams_escuchas
from funciones import mayores_streams_canciones
from funciones import mayores_streams_albums
from funciones import mayores_streams_musicos
from funciones import likes_playlist
from funciones import likes_cancion
from funciones import likes_album
from funciones import likes_musico
from funciones import buscador3
from funciones import buscador2
from funciones import buscador1
from funciones import borrar_perfil
from funciones import cambiar_perfil
from funciones import buscar_perfil
from funciones import original_datos
from funciones import guardar_data
from funciones import actualizar_datos
from funciones import carga_datos
RUTA_USUARIOS = "usuarios.json"
RUTA_ALBUMS = "albums.json"
RUTA_PLAYLIST = "playlist.json"


while True:
    LISTA_USUARIOS = carga_datos(RUTA_USUARIOS)
    LISTA_ALBUM = carga_datos(RUTA_ALBUMS)
    LISTA_PLAYLIST = carga_datos(RUTA_PLAYLIST)
    opcion = input(
        
        """Bienvenido a METROFY!
        ----------------------------
        -> 1. Gestión de perfiles
        -> 2. Gestión multimedia
        -> 3. Gestión de interacciones
        -> 4. Indicadores de gestion
        -> 0. Cargar datos de 0
        -> """)

    if opcion == "1":
        opcion_perfiles = input(
            """       -> 1. Registrar nuevo usuario
            -> 2. Buscar Perfiles
            -> 3. Cambiar información de la cuenta
            -> 4. Borrar datos de la cuenta
            -> """)

        if opcion_perfiles == "1":

            print("Vamos a registrarlo")
            print("A continuacion vamos a pedirle la informacion requerida")
            print("")
            tipoUsuario = input("Es cantante o escucha?: ")

            if tipoUsuario == 'cantante':
                archivo_nuevo = Cantante.nuevo_musico(RUTA_USUARIOS)
                actualizar_datos(archivo_nuevo, RUTA_USUARIOS)
                print("Se ha registrado con exito!")
            if tipoUsuario == 'escucha':
                archivo_nuevo = Escucha.nuevo_escucha(RUTA_USUARIOS)
                actualizar_datos(archivo_nuevo, RUTA_USUARIOS)
                print("Se ha registrado con exito!")

            


        elif opcion_perfiles == "2":

            print("Vamos a buscar un perfil")

            perfil_a_buscar = input("Indique el nombre de la persona a buscar: ")

            buscar_perfil(perfil_a_buscar)

        elif opcion_perfiles == "3":

            print("Vamos a cambiar la información personal de la cuenta.")
            print("")
            nombre_usuario_a_cambiar = input(
                "Indique el nombre del usuario que va a querer cambiar los datos: ")

            cambiar_perfil(nombre_usuario_a_cambiar)

        elif opcion_perfiles == "4":

            print("Vamos a borrar un usuario")
            print("Necesitaremos el nombre del usuario para borrar dicha cuenta")
            print("")
            nombre_usuario_a_borrar = input("Nombre: ")

            borrar_perfil(nombre_usuario_a_borrar)

    elif opcion == "2":
        opcion_musical = input("""
            -> 1. Crear nueva playlist
            -> 2. Crear nuevo album
            -> 3. Buscador
            -> """)

        if opcion_musical == "1":

            playlist_actual = Playlist.crear_playlist(RUTA_PLAYLIST)
            actualizar_datos(playlist_actual, RUTA_PLAYLIST)

        if opcion_musical == "2":

            album_actual = Album.crear_album(RUTA_ALBUMS)
            actualizar_datos(album_actual, RUTA_ALBUMS)

        if opcion_musical == "3":
            opcion_buscador = input("""
                -> 1. Buscar cancion por el nombre del album
                -> 2. Buscar cancion por el nombre de usuario
                -> 3. Buscar cancion por una playlist
                -> """)

            if opcion_buscador == '1':
                buscador1(RUTA_ALBUMS, RUTA_USUARIOS)
            if opcion_buscador == '2':
                buscador2(RUTA_ALBUMS, RUTA_USUARIOS)
            if opcion_buscador == '3':
                buscador3(RUTA_ALBUMS, RUTA_PLAYLIST, RUTA_USUARIOS)

    if opcion == '3':

        opcion_interacciones = input("""
            -> 1. Dar like a musico
            -> 2. Dar like a Album
            -> 3. Dar like a Cancion
            -> 4. Dar like a Playlist
                                       
            -> """)

        if opcion_interacciones == "1":

            print("")
            print("Vamos a dar like a un musico!")
            print("")

            likes_musico(LISTA_USUARIOS)

        if opcion_interacciones == "2":
            print("")
            print("Vamos a darle like a un Album!")

            likes_album(LISTA_USUARIOS, LISTA_ALBUM)

        if opcion_interacciones == '3':
            print("")
            print("Vamos a dar like a una cancion!")

            likes_cancion(LISTA_USUARIOS, LISTA_ALBUM)

        if opcion_interacciones == '4':

            print("")
            print("Vamos a dar like a una Playlist!")

            likes_playlist(LISTA_USUARIOS, LISTA_PLAYLIST)

    if opcion == "4":

        print("")
        print("Estos son los indicadores de gestion")
        print("Este módulo permitirá a los usuarios visualizar estadísticas sobre el desempeño de la plataforma")
        print("")

        opcion_indicadores = input("""
            -> 1. Top 5 de músicos con mayor cantidad de streams
            -> 2. Top 5 de álbumes con mayor cantidad de streams
            -> 3. Top 5 de canciones con mayor cantidad de streams
            -> 4. Top 5 de escuchas con mayor cantidad de streams
                                       
            -> """)

        if opcion_indicadores == "1":

            mayores_streams_musicos = mayores_streams_musicos(
                LISTA_USUARIOS, LISTA_ALBUM)
            print(mayores_streams_musicos)

        if opcion_indicadores == '2':

            mayores_streams_albums(LISTA_ALBUM)

        if opcion_indicadores == '3':

            mayores_streams_canciones(LISTA_ALBUM)

        if opcion_indicadores == '4':
            mayores_streams_escuchas(LISTA_USUARIOS, LISTA_ALBUM)
    
    if opcion == '0':
        original_datos()
