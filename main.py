# Script para google dorking



#Librerias
# Importo el módulo webbrowser para abrir páginas de búsqueda automáticamente en el navegador web
import webbrowser  # para las búsquedas con Google
# Importo time para gestionar los tiempos de espera y pausas en la ejecución de la consola
import time  # para tiempo de espera en la ejecución de consola
# Importo Fore de colorama para dar color y estilo visual a los mensajes en la consola
from colorama import Fore  # para dar color a la consola


# Bienvenida
# Hago una pausa de dos segundos antes de mostrar el mensaje de bienvenida
time.sleep(2)
print("\n")
print("\n")
# Imprimo el mensaje de bienvenida en color azul en la consola
print(Fore.BLUE + "Bienvenido al programa de Google Dorking automatizado")


# Variable para controlar si el programa sigue ejecutándose
# Inicializo la variable centinela en True para mantener activo el bucle principal de ejecución
seguir = True


while seguir:
    # Mostrar opciones
    # Pauso la ejecución temporalmente para dar fluidez visual al menú
    time.sleep(2)
    print("\n")
    print("Estas son las opciones para hacer Google Dorking con el navegador:")
    time.sleep(2)
    print("\n")
    print("1.Buscar url")
    print("2.Buscar titulo")
    print("3.Buscar pdf")
    print("4.Buscar jpg")
    print("5.Buscar todo url")
    print("6.Buscar contenido de la pagina")
    print("7.Buscar un sitio especifico")
    print("8.Buscar en la cache")


    # Preguntar por la info de cada opción
    time.sleep(2)
    print("\n")
    print("¿Quieres obtener información de alguna opción? (SI/NO)")
    # Capturo la respuesta del usuario para saber si requiere explicaciones adicionales
    respuesta_info = input("--->")


    #Si el usuario dice que si
    if respuesta_info.lower() == "si":
        time.sleep(2)
        print("\n")
        print("Pues elige una de las opciones:")
        time.sleep(2)
        print("\n")
        print("1.Buscar url")
        print("2.Buscar titulo")
        print("3.Buscar pdf")
        print("4.Buscar jpg")
        print("5.Buscar todo url")
        print("6.Buscar contenido de la pagina")
        print("7.Buscar un sitio especifico")
        print("8.Buscar en la cache")


        #Guardar la opcion del usuario en una variable
        # Almaceno el identificador de la opción sobre la cual el usuario pide detalles
        eleccion_info = input("--->")


        #Mostrar la informacion segun lo que haya ingresado el usuario
        #Para url
        if eleccion_info == "1":
            time.sleep(2)
            print("\n")
            print("Buscar url: Encuentra páginas que contengan una URL específica en su estructura.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 1")


       #Para intitle
        elif eleccion_info == "2":
            time.sleep(2)
            print("\n")
            print("Buscar título: Encuentra páginas web que tengan un título específico en la etiqueta <title>.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 2")


        #Para pdf
        elif eleccion_info == "3":
            time.sleep(2)
            print("\n")
            print("Buscar pdf: Busca archivos PDF relacionados con un término específico.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 3")


        #Para jpg
        elif eleccion_info == "4":
            time.sleep(2)
            print("\n")
            print("Buscar jpg: Encuentra imágenes en formato JPG relacionadas con un término específico.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 4")


        #Para allinurl
        elif eleccion_info == "5":
            time.sleep(2)
            print("\n")
            print("Buscar todo url: Busca páginas web que contengan una cadena específica en cualquier parte de la URL.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 5")


        #Para contenido en el body de una web
        elif eleccion_info == "6":
            time.sleep(2)
            print("\n")
            print("Buscar contenido de la página: Encuentra páginas que contengan un texto específico en su contenido.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 6")


        #Para buscar un sitio
        elif eleccion_info == "7":
            time.sleep(2)
            print("\n")
            print("Buscar un sitio específico: Realiza una búsqueda en un dominio específico para un término dado.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 7")


        #Para buscar en cache
        elif eleccion_info == "8":
            time.sleep(2)
            print("\n")
            print("Buscar en la cache: Muestra la versión en caché de una página web almacenada por Google.")
            time.sleep(2)
            print("\n")
            print("Muy bien pues elige abajo si quieres la opcion 8")


        else:
            time.sleep(2)
            print("\n")
            print("Opción no válida, por favor elige un número del 1 al 8.")


    if respuesta_info.lower() == "no":
        time.sleep(2)
        print("\n")
        print("Está bien, continuemos")
    

    #Si ingresa una opcion invalida
    else:
        time.sleep(2)
        print("\n")
        print("Esa no es una opcion valida")
        print("Tienes que responder si o no")


    # Recibir opción del usuario para usar una de las opciones en el navegador
    time.sleep(2)
    print("\n")
    print("Elige")
    # Leo la opción operativa que ejecuto en el navegador
    eleccion_usuario = input("--->")


    #Para url
    if eleccion_usuario == "1":
        time.sleep(2)
        print("\n")
        print("Dime una url para buscar")
        url = input("--->")
        # Construyo el operador de búsqueda inurl para filtrar por dirección
        buscar_1 = f"inurl:{url}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Lanzo la consulta generada directamente en Google usando mi navegador predeterminado
        webbrowser.open(f"https://www.google.com/search?q={buscar_1}")


    #Para intitle
    elif eleccion_usuario == "2":
        time.sleep(2)
        print("\n")
        titulo = input("Dime un título para buscar --->")
        # Formateo la consulta con intitle para buscar en los títulos de las páginas
        buscar_2 = f"intitle:{titulo}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Abro el navegador con el dork de título configurado
        webbrowser.open(f"https://www.google.com/search?q={buscar_2}")


    #Para pdf
    elif eleccion_usuario == "3":
        time.sleep(2)
        print("\n")
        pdf = input("Dime un pdf para buscar --->")
        # Armo el dork para buscar archivos PDF de un tema concreto
        buscar_3 = f"filetype:pdf {pdf}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Abro el navegador para buscar el documento PDF en la red
        webbrowser.open(f"https://www.google.com/search?q={buscar_3}")


    #Para jpg
    elif eleccion_usuario == "4":
        time.sleep(2)
        print("\n")
        jpg = input("Dime un jpg para buscar --->")
        # Configuro el dork para localizar ficheros de imagen formato JPG
        buscar_4 = f"filetype:jpg {jpg}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Ejecuto la búsqueda de imágenes en el navegador
        webbrowser.open(f"https://www.google.com/search?q={buscar_4}")


    #Para allinurl
    elif eleccion_usuario == "5":
        time.sleep(2)
        print("\n")
        url_completa = input("Dime una url completa para buscar --->")
        # Preparo la consulta usando allinurl para cadenas extensas en la ruta
        buscar_5 = f"allinurl:{url_completa}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Muestro los resultados del dork allinurl en el navegador
        webbrowser.open(f"https://www.google.com/search?q={buscar_5}")


    #Para contenido en el body de una web
    elif eleccion_usuario == "6":
        time.sleep(2)
        print("\n")
        contenido_pagina = input("Dime contenido de una página para buscar --->")
        # Utilizo intext para buscar cadenas de texto dentro del cuerpo del sitio
        buscar_6 = f"intext:{contenido_pagina}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Abro el navegador con la consulta de texto interno
        webbrowser.open(f"https://www.google.com/search?q={buscar_6}")


    #Para buscar un sitio
    elif eleccion_usuario == "7":
        time.sleep(2)
        print("\n")
        sitio_especifico = input("Dime un sitio específico para buscar --->")
        # Estructuro la orden site para restringir los resultados a un dominio en concreto
        buscar_7 = f"site:{sitio_especifico}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Ejecuto la consulta orientada a un sitio web en el navegador
        webbrowser.open(f"https://www.google.com/search?q={buscar_7}")


    #Para buscar en cache
    elif eleccion_usuario == "8":
        time.sleep(2)
        print("\n")
        cache = input("Dime cache para buscar --->")
        # Formo el dork de caché para consultar copias guardadas de páginas
        buscar_8 = f"cache:{cache}"
        time.sleep(2)
        print("\n")
        print("Muy bien en breve se verán las búsquedas...")
        time.sleep(4)
        # Muestro la versión en caché de la página web solicitada
        webbrowser.open(f"https://www.google.com/search?q={buscar_8}")


    #Si la opcion es invalida
    else:
        time.sleep(2)
        print("\n")
        print("Esa no es una opción válida")
        time.sleep(2)
        print("\n")
        print("Tienes que ingresar un número del 1 al 8")


    # Preguntar al usuario si quiere continuar
    time.sleep(2)
    print("\n")
    print("¿Quieres seguir? (SI/NO)")
    eleccion_usuario2 = input("--->")

    # Compruebo si decido salir del bucle en función de la respuesta obtenida
    if eleccion_usuario2.lower() not in ["si", "s"]:
        seguir = False


#La despedida
time.sleep(2)
print("\n")
print("Gracias por usar este programa!")
