def lista_de_productos():
    lista_productos = []

    while True:
        print("Lista de productos:")
        for i, item in enumerate(lista_productos):
            print(f"{i + 1}. {item}")

        print("Opciones:")
        print("1. Añadir ítem")
        print("2. Eliminar ítem")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            nuevo_item = input("Ingresa el nuevo ítem: ")
            lista_productos.append(nuevo_item)
        elif opcion == "2":
            if len(lista_productos) > 0:
                indice_eliminar = int(input("Ingresa el número del ítem a eliminar: "))
                if 1 <= indice_eliminar <= len(lista_productos):
                    lista_productos.pop(indice_eliminar - 1)
                else:
                    print("Índice no válido. Inténtalo de nuevo.")
            else:
                print("La lista está vacía.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


lista_de_productos()
