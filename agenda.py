def agregar_contacto(agenda):
    """Permite al usuario agregar un nuevo contacto a la agenda."""
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el número de teléfono: ")
    agenda[nombre] = telefono
    print(f"✅ Contacto '{nombre}' agregado con éxito.")

def buscar_contacto(agenda):
    """Busca y muestra la información de un contacto por su nombre."""
    nombre = input("Ingresa el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"📞 Contacto encontrado: {nombre} - {agenda[nombre]}")
    else:
        print(f"❌ Contacto '{nombre}' no encontrado.")

def mostrar_contactos(agenda):
    """Muestra todos los contactos de la agenda en orden alfabético."""
    if not agenda:
        print("La agenda está vacía.")
        return

    print("--- Agenda de Contactos ---")
    nombres_ordenados = sorted(agenda.keys())
    for nombre in nombres_ordenados:
        print(f"{nombre}: {agenda[nombre]}")
    print("-------------------------")

def main():
    """Función principal que ejecuta el menú interactivo."""
    agenda = {}
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            buscar_contacto(agenda)
        elif opcion == '3':
            mostrar_contactos(agenda)
        elif opcion == '4':
            print("Saliendo de la agenda. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()