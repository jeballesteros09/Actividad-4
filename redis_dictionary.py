import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)


def agregar_palabra():
    palabra = input("Ingrese la palabra a agregar: ")
    significado = input("Ingrese el significado: ")
    r.hset('dictionary', palabra, significado)
    print(f"{palabra} agregada al diccionario.")


def editar_palabra():
    palabra = input("Ingrese palabra a modificar: ")
    significado = input("Ingrese el nuevo significado de la palabra: ")
    r.hset('dictionary', palabra, significado)
    print(f"{palabra} actualizada en el diccionario.")


def eliminar_palabra():
    palabra = input("Ingrese la palabra a remover: ")
    r.hdel('dictionary', palabra)
    print(f"{palabra} eliminada del diccionario.")


def buscar_palabra():
    palabra = input("Ingrese la palabra a buscar: ")
    significado = r.hget('dictionary', palabra)
    if significado:
        print(f"{palabra}: {significado.decode()}")
    else:
        print(f"{palabra} no esta presente en el diccionario.")


def ver_diccionario():
    words = r.hgetall('dictionary')
    if words:
        for palabra, significado in words.items():
            print(f"{palabra.decode()}: {significado.decode()}")
    else:
        print("El diccionario esta vacio.")


def display_menu():
    print("1. Agregar palabra")
    print("2. Editar palabra")
    print("3. Remover palabra")
    print("4. Buscar palabra")
    print("5. Ver todas las palbras")
    print("6. Salir")


while True:
    display_menu()
    choice = input("Ingrese su eleccion: ")

    if choice == '1':
        agregar_palabra()
    elif choice == '2':
        editar_palabra()
    elif choice == '3':
        eliminar_palabra()
    elif choice == '4':
        buscar_palabra()
    elif choice == '5':
        ver_diccionario()
    elif choice == '6':
        break
    else:
        print("Eleccion no valida. Por favor, intente de nuevo.")
